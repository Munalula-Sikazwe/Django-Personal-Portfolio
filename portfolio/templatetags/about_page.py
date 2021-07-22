from django.template import Library

from portfolio.models import AboutMe

register = Library()


@register.inclusion_tag("Partials/_aboutme_section.html")
def get_about_data():
    aboutme = AboutMe.objects.first()
    return {"aboutme": aboutme}

@register.inclusion_tag("Partials/_introduction_section.html")
def get_introduction_data():
    aboutme = AboutMe.objects.first()
    return {"aboutme": aboutme}
