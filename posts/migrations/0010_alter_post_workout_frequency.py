# Generated by Django 4.2.16 on 2024-12-17 17:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_post_equipment_available_post_nutrition_focus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='workout_frequency',
            field=models.IntegerField(blank=True, default=2, help_text='How many times do you workout per week?', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)]),
        ),
    ]