# Generated by Django 3.1.5 on 2021-07-23 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_aboutme_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='img_link',
            field=models.URLField(default='#', max_length=100),
        ),
    ]
