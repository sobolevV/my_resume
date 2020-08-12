from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    content = RichTextUploadingField(blank=True)
    url = models.URLField(max_length=300, blank=True)
    date = models.DateField(auto_now_add=True)