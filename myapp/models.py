from django.db import models

# Create your models here.
class MyModel(models.Model):
    photo = models.ImageField()