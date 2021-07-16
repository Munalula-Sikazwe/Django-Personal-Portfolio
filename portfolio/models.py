from django.db import models

# Create your models here.
class AboutMe(models.Model):
    class Meta:
        verbose_name_plural = "About Me Section"
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    interest1 = models.TextField(max_length=500)
    interest2 = models.TextField(max_length=500)
    def __str__(self):
        return self.name
class Service(models.Model):
    title = models.CharField(max_length=100)
    tools = models.CharField(max_length=200)

