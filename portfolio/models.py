from django.db import models
def get_folder_name(instance,filename):
    return instance.title
def get_profile_name(instance,filename):
    return instance.name +  '_photo'
# Create your models here.
class AboutMe(models.Model):
    class Meta:
        verbose_name_plural = "AboutMe"

    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    interest1 = models.TextField(max_length=500)
    interest2 = models.TextField(max_length=500)
    email = models.EmailField(max_length=200, null=True)
    address = models.CharField(max_length=200, default="UnAvailable")
    phone_no = models.CharField(max_length=15,default="UnAvailable")
    photo = models.ImageField(upload_to=get_profile_name,null=True)
    resume = models.FileField(upload_to='cv',null=True)
    certification = models.FileField(upload_to='certification',null=True)
    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=100)
    tools = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.CharField(max_length=100)
    link = models.URLField(max_length=100)
    img_link = models.URLField(max_length=100,default="unAvailable")
    description = models.TextField(max_length=100)
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    def __str__(self):
        return self.name


class Education(models.Model):
    class Meta:
        verbose_name_plural = "Education"

    qualification = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    def __str__(self):
        return  self.qualification


class Experience(models.Model):
    position = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    def __str__(self):
        return self.position


class Expertise(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Work(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    link = models.URLField(max_length=100)
    img = models.ImageField(upload_to=get_folder_name,null=True)
    def __str__(self):
        return self.title
class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=3)
