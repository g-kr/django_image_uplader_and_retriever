from django.db import models
from django.db.models.base import Model
from django.db.models.fields.files import ImageField

# Create your models here.
class Uimage(models.Model):
    image = models.ImageField(upload_to="myimage")
    date  = models.DateTimeField(auto_now_add=True)