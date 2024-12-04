from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all().order_by("-created_on")
    template_name = "posts/index.html"
    paginate_by = 6

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

    return render(
        request,
        "posts/post_detail.html",
        {"post": post},
    )

