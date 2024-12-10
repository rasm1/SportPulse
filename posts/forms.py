from .models import Comment, Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug','content','topic']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)