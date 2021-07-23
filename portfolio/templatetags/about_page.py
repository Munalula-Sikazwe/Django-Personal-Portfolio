from django.template import Library
from portfolio import models

register = Library()


@register.inclusion_tag("Partials/_aboutme_section.html")
def get_about_data():
    aboutme = models.AboutMe.objects.first()
    services = models.Service.objects.all()
    return {"aboutme": aboutme,"services":services}

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

