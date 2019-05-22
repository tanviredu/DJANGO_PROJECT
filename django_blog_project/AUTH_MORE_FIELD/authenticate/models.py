from django.conf import settings
from django.db import models
## we import the database
##the moment we post it is need to we import timezone too
from django.utils import timezone
# Create your models here.
## we need the by bdefault user database
from django.contrib.auth.models import User
#you can import it like that but for foreign key 
#you have to make it differently
#now create the class

class Post(models.Model):
    ## we need the title of the post
    title = models.CharField(max_length=200)
    ## content
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True)

    ## and we need the author
    #its the user of the content
    #we fetch it or add with the Foreign Key with the default user database

    ## the user model will be
    author =models.ForeignKey(User,on_delete=models.CASCADE)



    def publish(self):
        ##this function will afor automatically add that time 
        ## when posting
        self.published_date = timezone.now()
        self.save()
        ## for saving everything
    
    #we need a decoretor for convenince
    def __str__(self):
        return self.title
    

    ## ok the databse created now add in the adminsection