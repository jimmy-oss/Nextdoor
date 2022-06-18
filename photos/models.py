from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from phone_field import PhoneField
import uuid
from datetime import datetime

User = get_user_model() 
 
# Create your models here.
class Category (models.Model):
     name = models.CharField(max_length=100, null=False,blank=False)
     
  
def __str__ (self):
      return self.name

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='profile')
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    phone_number = PhoneField(blank=True, help_text=' Emergency Contacts')
    email_address = models.EmailField(max_length=150,blank=True)
    location = models.CharField(max_length=100, blank=True)
    neighbour_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
     
class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
      
class Photo (models.Model):
     category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
     image = CloudinaryField('image')
     description = models.TextField()
     email_address = models.EmailField(max_length=150,blank=True)
      
     
def __str__ (self):
      return self.description 