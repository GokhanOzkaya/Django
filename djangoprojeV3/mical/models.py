from django.db import models

# Create your models here.

class mical(models.Model):
    ad=models.CharField(max_length=50)
    soyad=models.CharField(max_length=50)
    açıklama=models.CharField(max_length=50)