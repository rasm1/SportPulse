from django.db import models
from django.contrib.auth.models import User

TOPIC = ((0, "advice", 1, "diet", 2, "form",3,"training schedules", 5, " "))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # related name = raar
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    topic = models.IntegerField(choices=TOPIC, default = 5)