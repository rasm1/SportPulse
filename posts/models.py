from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

# Sets of tuples to create choises for custom properties
TOPIC = ((0, "advice"), (1, "diet"), (2, "form"),
         (3, "training schedules"), (4, " "))

SUBTOPICS = ((0, "warm-up"), (1, "choosing the right gym"),
             (2, "fitness goals"), (3, "tips and tricks"), (4, "consistency"),
             (5, "injuries"), (6, "recovery meals"), (7, "meal prep"),
             (8, "supplements"),
             (9, "fat loss"), (10, "hydration"), (11, "macros"),
             (12, "calories"), (13, "basics"),
             (14, "proper posture"), (15, "breathing techniques"),
             (16, "common mistakes"), (17, "safety"), (18, "mobility"),
             (19, "full body"), (20, "push-pull-legs"),
             (21, "progressive overload"),
             (22, "cardio"), (23, "strength"), (24, "HIIT"),
             (25, "planning"), (26, "upper/lower"))

EQUIPMENT_AVAILABLE = ((0, "none"), (1, "dumbbells"), (2, "barbell"),
                       (3, "resistance_bands"), (4, "machines"),
                       (5, "kettlebells"),
                       (6, "bodyweight"), (7, "yoga_mat"), (8, "plates"),
                       (9, "upright_bike"), (10, "treadmill"))


# model for Posts

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    topic = models.IntegerField(choices=TOPIC, default=4, blank=True)
    subtopics = MultiSelectField(choices=SUBTOPICS, blank=True)
    experience_level = models.CharField(max_length=50, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('professional', 'Professional')
    ],
        default='beginner',
        blank=True)
    goal = models.CharField(
        max_length=50,
        choices=[
            ('weight_loss', 'Weight Loss'),
            ('hypertrophy', 'Hypertrophy'),
            ('endurance', 'Endurance'),
            ('cardio', 'Cardio'),
            ('strength', 'Strength Training'),
            ('general_fitness', 'General Fitness'),
            ('flexibility', 'Flexibility'),
            ('mobility', 'Mobility')
        ],
        default='general_fitness',
        blank=True
    )
    equipment_available = MultiSelectField(choices=EQUIPMENT_AVAILABLE,
                                           blank=True)
    nutrition_focus = models.CharField(
        max_length=50,
        choices=[
            ('none', 'None'),
            ('weight_loss', 'Weight Loss'),
            ('muscle_building', 'Muscle Building'),
            ('balanced', 'Balanced Diet'),
        ],
        default='none',
        blank=True
    )
    workout_frequency = models.IntegerField(
        default=2,
        blank=True,
        help_text="How many times do you workout per week?",
        validators=[MinValueValidator(0), MaxValueValidator(7)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


# model for comments

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment, {self.body} by {self.author}"
