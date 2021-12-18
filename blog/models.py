from django.db import models
from taggit.managers import  TaggableManager
from  django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author      = models.ForeignKey(User, related_name='post_author', on_delete = models.CASCADE)
    title       = models.CharField(max_length = 100)
    tags        = TaggableManager()
    image        = models.ImageField(upload_to = 'post/')
    crated_at   = models.DateTimeField(default = timezone.now)
    description = models.TextField(max_length=20000)
    category    = models.ForeignKey('Category' , related_name = 'post_category',on_delete = models.CASCADE)
    slug        = models.SlugField(null = True , blank = True)
    
    
    def  __str__(self):
        return self.title
    
    
    
    
    
    # دالة تحويل اسم المقال الي رابط وازالة المسافات الفارغة ووضع - داش-----
    def save(self, *args, **kwargs):
        from django.utils.text import slugify
        if not self.slug:
            self.slug = slugify (self.title)
        super(Post, self).save(*args, **kwargs) # Call the real save() method
    
    #-----------------------------------------------------------------------------
    
        
        # دالة جلب رابط المقال -------------------------------- 
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
        #-----------------------------------------------------------
    
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
