from django.db import models

# Create your models here.
class places(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name
class team(models.Model):
    tname=models.CharField(max_length=200)
    timage=models.ImageField(upload_to='pic')
    tdesc=models.TextField()

    def __str__(self):
        return self.tname