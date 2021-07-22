from django.template import Library
from portfolio.models import AboutMe
register = Library()

@register.inclusion_tag('Partials/_aboutme_section.html')
def get_about_date():
    aboutme = AboutMe.objects.all()
    return {"aboutme":aboutme}