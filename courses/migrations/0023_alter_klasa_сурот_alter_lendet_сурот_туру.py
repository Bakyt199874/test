# Generated by Django 4.0.5 on 2022-06-25 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0022_alter_lesson_видео'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klasa',
            name='Сурот',
            field=models.ImageField(default='cat_images/1.jpg', upload_to='cat_images'),
        ),
        migrations.AlterField(
            model_name='lendet',
            name='Сурот_туру',
            field=models.ImageField(default='1.jpg', upload_to='kurs_images'),
        ),
    ]
