from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phnum = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    PCM = models.CharField(max_length=10)
    ProfilePicture = models.ImageField(upload_to='')
    Description = models.CharField(max_length=150)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
      ordering = ['name']