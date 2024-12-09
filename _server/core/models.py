from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Session(models.Model):
    token = models.TextField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Character(models.Model):
    name= models.TextField()
    review = models.TextField(blank=True)
    rating = models.IntegerField(default=3)
    share_publically = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Image(models.Model):
    link = models.TextField(default="")
    character =models.ForeignKey(Character, on_delete=models.CASCADE)
