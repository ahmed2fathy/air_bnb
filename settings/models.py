from django.db import models
from distutils.command import upload

# Create your models here.

class Settings(models.Model):
    site_name      = models.CharField(max_length = 100)
    logo           = models.ImageField (upload_to = 'settings/')
    phone          = models.CharField(max_length = 20)
    email          = models.EmailField(max_length = 254)
    description    = models.TextField(max_length = 500)
    fb_link        = models.URLField(max_length = 400)
    twitter_link   = models.URLField(max_length = 400)
    instagram_link = models.URLField(max_length = 400)
    
    
    
    
    def  __str__(self):
            return self.site_name
