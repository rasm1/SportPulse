from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm


# views
class PostList(generic.ListView):
    queryset = Post.objects.all().order_by("-created_on")
    template_name = "posts/index.html"
    paginate_by = 6


@login_required
def create_post(request):
    """"
     View to create a post

    """

    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post submitted succesfully!'
            )
            return redirect('home')

        else:
            messages.add_message(
                request, messages.ERROR,
                'post was not submitted'
            )

    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def post_edit(request, slug, post_id):
    """
    view to edit post
    """
    form = PostForm()
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)

    if post.author != request.user:
            messages.add_message(request,
                                 messages.ERROR,
                                 'You can only edit your own posts!')
            return redirect('home')

    if request.method == "POST":

        form = PostForm(data=request.POST, instance=post)

        if form.is_valid() and post.author == request.user:
            post = form.save(commit=False)
            post = post
            post.author = request.user
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Post Updated!')
            return redirect('home')

        else:
            return redirect('home')
            messages.add_message(request, messages.ERROR,
                                 'Error updating post!')

    else:
        form = PostForm(instance=post)

    return render(request, 'posts/edit_post.html', {'form': form,
                                                    'post': post})


@login_required
def post_delete(request, slug, post_id):
    """
    view to delete post
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug, id=post_id)

    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Post deleted!')
        return redirect('home')

    else:
        return redirect("home")
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own Posts!')

    return redirect('home')


def post_detail(request, slug):
    """
    Display an individual :model:`posts.Post`.

    **Context**

    ``post``
        An instance of :model:`posts.Post`.

    **Template:**

    :template:`posts/post_detail.html`
    """

    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted succesfully!'
            )
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

        else:
            messages.add_message(
                request, messages.ERROR,
                'comment was not submitted'
            )

    else:
        comment_form = CommentForm()

    return render(
        request,
        "posts/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
        }
    )


@login_required
def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """

    if request.method == "POST":
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
            return redirect('post_detail', slug=slug)
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def custom_handler404(request, exception):
    """
    Custom handler for 404 (Page Not Found) errors.
    """
    return render(request, '404.html', status=404)


def custom_handler500(request):
    """
    Custom handler for 500 (Internal Server Error) errors.
    """
    return render(request, '500.html', status=500)
