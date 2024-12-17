# Generated by Django 4.2.16 on 2024-12-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_experience_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='goal',
            field=models.CharField(blank=True, choices=[('weight_loss', 'Weight Loss'), ('muscle_gain', 'Muscle Gain'), ('endurance', 'Endurance'), ('strength', 'Strength Training'), ('general_fitness', 'General Fitness'), ('flexibility', 'Flexibility')], default='general_fitness', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='workout_frequency',
            field=models.IntegerField(blank=True, default=2, help_text='How many times do you workout per week?'),
        ),
    ]
