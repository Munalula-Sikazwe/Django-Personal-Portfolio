# Generated by Django 3.1.5 on 2021-07-16 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
            ],
        ),
    ]