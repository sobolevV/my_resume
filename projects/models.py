from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.sitemaps import ping_google


class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    content = RichTextUploadingField(blank=True)
    url = models.URLField(max_length=300, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Project: {self.name}"

    def save(self, force_insert=False, force_update=False):
        super().save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass