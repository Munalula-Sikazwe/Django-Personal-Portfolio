from django.db import models

# Create your models here.
class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    interest1 = models.TextField(max_length=500)
    interest2 = models.TextField(max_length=500)
