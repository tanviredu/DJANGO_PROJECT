from django.db import models

## importing the user database
from django.contrib.auth.models import User

class Admin(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    
    def __str__(self):
        return self.name
class Department(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    
    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name="department +")
    
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=150)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name="doctor +")
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name="department +")
    time = models.DateTimeField()
    def __str__(self):
        return self.name