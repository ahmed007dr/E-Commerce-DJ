from django.db import models

# Create your models here.

class Settings(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='settings')
    width_logo = models.ImageField(upload_to='settings',null=True,blank=True)
    subtitle = models.TextField(max_length=500)
    call_us = models.CharField(max_length=25)
    emails_us = models.TextField(max_length=25)
    emails = models.TextField(max_length=50)
    phone = models.TextField(max_length=50)
    address = models.TextField(max_length=100)
    android_app = models.URLField(null=True,blank=True)
    ios_app = models.URLField(null=True,blank=True)
    facebook = models.URLField(null=True,blank=True)
    youtube = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name
    
class Locations(models.Model):
    name = models.CharField(max_length=30)
    details_name = models.CharField(max_length=200)

class DeliveryFee(models.Model):
    location = models.OneToOneField(Locations,related_name='fee_location',on_delete=models.CASCADE)
    fee=models.IntegerField()
    
    def __str__(self):
        return str(self.fee)