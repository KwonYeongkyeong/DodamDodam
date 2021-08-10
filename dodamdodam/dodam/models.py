
from django.db import models

# Create your models here.

class answer(models.Model):
    q1 = models.CharField(max_length=200)
    q2 = models.CharField(max_length=200)
    q3 = models.CharField(max_length=200)
    picture = models.CharField(max_length=100)