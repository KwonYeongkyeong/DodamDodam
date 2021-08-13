from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class answer(models.Model):
    pub_date = models.DateTimeField('data published')
    q1 = models.CharField(max_length=200)
    q2 = models.CharField(max_length=200)
    q3 = models.CharField(max_length=200)
    picture = models.CharField(max_length=100)
    ans = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.writer)+" : "+str(self.pub_date)
        
class Picture(models.Model):
    draw = models.ImageField(blank=True, upload_to="images", null=True)