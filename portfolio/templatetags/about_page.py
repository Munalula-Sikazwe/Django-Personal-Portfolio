from django.template import Library

from portfolio import models

register = Library()


@register.inclusion_tag("Partials/_aboutme_section.html")
def get_about_data():
    aboutme = models.AboutMe.objects.first()
    services = models.Service.objects.all()
    return {"aboutme": aboutme, "services": services}


@register.inclusion_tag("Partials/_introduction_section.html")
def get_introduction_data():
    aboutme = models.AboutMe.objects.first()
    return {"aboutme": aboutme}


@register.inclusion_tag("Partials/_expertise_section.html")
def get_expertise_data():
    expertise = models.Expertise.objects.all()
    return {"expertise": expertise}


@register.inclusion_tag("Partials/_education_section.html")
def get_education_data():
    education = models.Education.objects.all()
    return {"education": education}


@register.inclusion_tag("Partials/_experience_section.html")
def get_experience_data():
    experience = models.Experience.objects.all()
    return {"experience": experience}


@register.inclusion_tag("Partials/_work_section.html")
def get_work_data():
    works = models.Work.objects.all()
    return {"works": works}


@register.inclusion_tag("Partials/_blog_section.html")
def get_blog_data():
    blogs = models.Blog.objects.all()
    return {"blogs": blogs}

@register.inclusion_tag("Partials/_contact_section.html")
def get_contact_data():
    contacts = models.Contact.objects.first()
    return {"contacts": contacts}

