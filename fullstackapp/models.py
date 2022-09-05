from django.db import models

# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=200)
    origin = models.CharField(max_length=200) 
    details = models.CharField(max_length=200)

class contactDetails(models.Model):
    name= models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=200,null=True)
    number = models.IntegerField(null=True)
    subject = models.CharField(max_length=200,null=True)
    text = models.TextField(null=True)