from .models import Comment, Post
from django import forms


class PostForm(forms.ModelForm):
    workout_frequency = forms.IntegerField(
        min_value=0, max_value=7,
        help_text="How many times do you workout per week?")

    class Meta:
        model = Post
        fields = ['title', 'content', 'topic',
                  'subtopics', 'experience_level',
                  'goal', 'workout_frequency', 'equipment_available',
                  'nutrition_focus']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body'),
