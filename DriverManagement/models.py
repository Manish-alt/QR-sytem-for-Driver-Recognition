from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

#User refers to the officers who uses the application
class User(models.Model):
    first_name = models.CharField(max_length=100, )
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone} {self.email} {self.password}'
    
    
    
    
# Profile of the officers
class OfficerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user
    
    
# Create Officer Profile
def create_officer_profile(sender, instance, created, **kwargs):
    if created:
        officer_profile = OfficerProfile.objects.create(user = instance)
        officer_profile.save()
        
post_save.connect(create_officer_profile, sender=User)


# Driver details 
class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    profile_picture = models.ImageField(upload_to='upload/driver_profile_pictures/')
    