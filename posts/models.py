from django.db import models
from django.contrib.auth.models import User

TOPIC = ((0, "advice"),( 1, "diet"),( 2, "form"),(3,"training schedules"),( 4, " "))

# Create your models here.
# to do: add tags, likes, dislikes
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # related name = raar
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    topic = models.IntegerField(choices=TOPIC, default = 4)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"{self.title} | written by {self.author}"
    # could you django-taggit for tags but could cause issue cause
    # issue because we use postgress instead of sqlite

#to do: add likes/dislikes
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"Comment, {self.body} by {self.author}"