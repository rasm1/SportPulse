from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

TOPIC = ((0, "advice"),( 1, "diet"),( 2, "form"),(3,"training schedules"),( 4, " "))
SUBTOPICS = ((0,"warm-up"),(1,"choosing the right gym"),(2,"fitness goals"),(3,"tips and tricks"),(4,"consistency"),(5,"injuries"),(6,"recovery meals"),(7,"meal prep"),(8,"supplements"),
(9,"fat loss"),(10,"hydration"),(11,"macros"),(12,"calories"),(13,"basics"),(14,"proper posture"),(15,"breathing techniques"),(16,"common mistakes"),(17,"safety"),(18,"mobility"),
(19,"full body"),(20,"push-pull-legs"),(21,"progressive overload"),(22,"cardio"),(23,"strength"),(24,"HIIT"),(25,"planning"),(26,"upper/lower"))

 

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
    topic = models.IntegerField(choices=TOPIC, default = 4, blank=True)
    subtopics = MultiSelectField(choices=SUBTOPICS, blank=True)
    
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