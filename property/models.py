
from django.db import models
from  django.contrib.auth.models import User
from  django.utils import timezone
# Create your models here.
# 

class Property(models.Model):
    name        = models.CharField(max_length = 100)
    image       = models.ImageField(upload_to ='property/')
    price       = models.IntegerField(default = 0)
    description = models.TextField(max_length = 10000)
    place       = models.ForeignKey('place', related_name = 'property_place' , on_delete = models.CASCADE)
    category    = models.ForeignKey('category' , related_name = 'propery_category' , on_delete = models.CASCADE)
    slug        = models.SlugField(null = True , blank = True)
    crated_at = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.name
    
    
    
    # دالة تحويل اسم المقال الي رابط وازالة المسافات الفارغة ووضع - داش 
    
    def save(self, *args, **kwargs):
        from django.utils.text import slugify
        if not self.slug:
            self.slug = slugify (self.name)
         
        super(Property, self).save(*args, **kwargs) # Call the real save() method
        
    #-----------------------------------------------------------------------------
    
    
    # دالة جلب رابط المقال
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('property:property_detail', kwargs={'slug': self.slug})
        
    #--------------------------------------------------------
    
    
    
    
    
    
class PropertyImages(models.Model):
    Property  = models.ForeignKey(Property , related_name ='property_images',on_delete = models.CASCADE)
    image = models.ImageField(upload_to ='property_images/')
    
    def __str__(self):
        return str (self.Property)



class Place(models.Model):
    name  = models.CharField(max_length = 50)
    image = models.ImageField(upload_to ='places/')
    
    def __str__(self):
        return self.name
    
    
    
class Category(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name
    
    
    
class PropertyReview(models.Model):
    author    = models.ForeignKey(User, related_name ='review_author' , on_delete = models.CASCADE)
    Property  = models.ForeignKey(Property , related_name ='review_property', on_delete = models.CASCADE)
    rate      = models.IntegerField(default = 0)
    feedback  = models.TextField(max_length = 2000)
    crated_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return str (self.Property)
   
   
   
COUNT = (
(1,1),
(2,2),
(3,3),
(4,4)  ) 
    
class  PropertyBook(models.Model):
    user = models.ForeignKey(User, related_name ='book_owner' , on_delete = models.CASCADE)
    Property  = models.ForeignKey(Property , related_name ='book_property', on_delete = models.CASCADE)
    date_form = models.DateField(default = timezone.now)
    date_to   = models.DateField(default = timezone.now)
    guest     = models.CharField(max_length=2, choices = COUNT )
    children  = models.CharField(max_length=2, choices = COUNT )
    
    def __str__(self):
        return str (self.Property)