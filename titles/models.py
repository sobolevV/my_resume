from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Title(models.Model):
    name = models.CharField(max_length=200, null=False)
    content = RichTextUploadingField(null=False)
