# Generated by Django 3.1.5 on 2021-07-16 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('interest1', models.TextField(max_length=500)),
                ('interest2', models.TextField(max_length=500)),
            ],
        ),
    ]
