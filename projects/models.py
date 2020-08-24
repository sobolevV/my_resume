from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    content = RichTextUploadingField(blank=True)
    url = models.URLField(max_length=300, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Project: {self.name}"

    def get_absolute_url(self):
        return reverse('projects:description',
                       args=[self.id])