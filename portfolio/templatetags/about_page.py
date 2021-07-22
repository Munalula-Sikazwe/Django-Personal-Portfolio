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

