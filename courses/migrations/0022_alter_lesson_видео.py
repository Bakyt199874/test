# Generated by Django 4.0.5 on 2022-06-22 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0021_alter_lesson_видео'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='Видео',
            field=models.FileField(default='videos/1.mp4', upload_to='videos/'),
        ),
    ]
