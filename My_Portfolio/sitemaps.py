from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticPageSites(Sitemap):
    def items(self):
        return ['home']
    def location(self, items):
        return reverse(items)