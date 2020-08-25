from django.contrib import sitemaps
from django.urls import reverse
from projects.models import Project


class ProjectsSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.date


class StaticSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return 'mainapp:index'

    def location(self, item):
        return reverse(item)