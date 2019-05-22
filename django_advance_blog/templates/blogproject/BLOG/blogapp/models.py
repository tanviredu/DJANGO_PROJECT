from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Catagory(models.Model):
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    
    
    def __str__(self):
        
        return self.name




class Post(models.Model):
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateField()
    image = models.ImageField(upload_to='product/%Y/%m/%d',blank=True)
    
    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.CharField(max_length=150)
    job_title=models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='product/%Y/%m/%d',blank=True)

    def __str__(self):
        return str(self.name)







