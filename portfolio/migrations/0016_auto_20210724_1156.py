# Generated by Django 3.1.5 on 2021-07-24 11:56

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_aboutme_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='img_link',
        ),
        migrations.AddField(
            model_name='work',
            name='img',
            field=models.ImageField(null=True, upload_to=portfolio.models.get_folder_name),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='photo',
            field=models.ImageField(null=True, upload_to=portfolio.models.get_profile_name),
        ),
    ]