from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all().order_by("-created_on")
    template_name = "posts/index.html"
    paginate_by = 6

def create_post(request):
    """"
     View to create a post 
    
    """


    if request.method == "POST":
        form = PostForm(data = request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
            messages.add_message(
            request, messages.SUCCESS,
            'Post submitted succesfully!'
    )

    else:
        form = PostForm()
        messages.add_message(
            request, messages.ERROR,
            'post was not submitted'
        )
    return render(request, 'posts/create_post.html', {'form': form})


def post_edit(request, slug, post_id):
    """
    view to edit post
    """
    form = PostForm()
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    if request.method == "POST":

        
        form = PostForm(data = request.POST)

        if  form.is_valid() and post.author == request.user:
            post = form.save(commit=False)
            post = post
            post.save()
            return redirect('home')
            messages.add_message(request, messages.SUCCESS, 'Post Updated!')
        else:
            form = PostForm()
            messages.add_message(request, messages.ERROR, 'Error updating post!')

    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})



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
    # bugged: always displays the message 
    else:
        messages.add_message(
            request, messages.ERROR,
            'comment was not submitted'
        )

    

    return render(
        request,
        "posts/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_form": comment_form,
        
        }
    )

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
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

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
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))