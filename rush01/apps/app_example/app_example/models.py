from django.db import models
from django.conf import settings
# Create your models here.

class Image(models.Model):
    docfile = models.FileField(upload_to="")
