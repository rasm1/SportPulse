from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

TOPIC = ((0, "advice"),( 1, "diet"),( 2, "form"),(3,"training schedules"),( 4, " "))
SUBTOPICS = {
    0: ["warm-up", "choosing the right gym", "fitness goals", "tips and tricks", "consistency","injuries"],
    1: ["recovery meals", "meal prep", "supplements", "fat loss", "hydration","macros","calories"],
    2: ["bench press basics","proper posture","breathing techniques","common mistakes","safety","mobility"],
    3: ["full body","Push-pull-legs","progresive overload","cardio","strength","HIIT","planning","upper/lower split"]
}   
# Create your models here.
# to do: add tags, likes, dislikes
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
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