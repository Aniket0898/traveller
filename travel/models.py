from distutils.command.upload import upload
from django.db import models

# Create your models here.

class destination(models.Model):
    idvalue = models.IntegerField()
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pictures')
    thoughts = models.TextField()
    price = models.IntegerField()
    more = models.URLField()
    Description = models.TextField()