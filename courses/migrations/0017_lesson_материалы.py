# Generated by Django 4.0.5 on 2022-06-21 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_rename_pershkrimi_klasa_ачыктоо_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='Материалы',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
