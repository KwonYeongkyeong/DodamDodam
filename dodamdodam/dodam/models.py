
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.

class answer(models.Model):
    q1 = models.CharField(max_length=200)
    q2 = models.CharField(max_length=200)
    q3 = models.CharField(max_length=200)
    picture = models.CharField(max_length=100)

class Picture(models.Model):
    draw = models.ImageField(blank=True, upload_to="images", null=True)