# Generated by Django 4.2.16 on 2024-12-17 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='experience_level',
            field=models.CharField(blank=True, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='beginner', max_length=50),
        ),
    ]
