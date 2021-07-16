from django.db import models


# Create your models here.
class AboutMe(models.Model):
    class Meta:
        verbose_name_plural = "About Me Section"

    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    interest1 = models.TextField(max_length=500)
    interest2 = models.TextField(max_length=500)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=100)
    tools = models.CharField(max_length=200)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.CharField(max_length=100)
    link = models.URLField(max_length=100)
    description = models.TextField(max_length=100)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)


class Education(models.Model):
    qualification = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

