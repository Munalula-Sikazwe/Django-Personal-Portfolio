# Generated by Django 3.1.5 on 2021-07-23 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_work_img_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='img_link',
            field=models.URLField(default='unAvailable', max_length=100),
        ),
    ]
