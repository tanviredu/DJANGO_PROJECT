from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Post(models.Model):

	## this is the tricy part
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	## the authors is a user and pull username from the user 
	## and if the user is delete all the user post will be delete
	## thats why its a class of 'auth.User'
	## and on_delete=models.CASCADE
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(datetime.datetime.now())
	published_date = models.DateTimeField(blank=True,null=True)
	## we leave it empty we add it in the publish function

	## and there will be a function called publish 
	## which publish or save the thing 
	## we are not going to take this on the views.py
	def publish(self):
		self.published_date = datetime.datetime.now()
		self.save()

		## if you want to do it on the views
		## we have to use Post.save()
		##  so in the models in the self.save()

	## published with respect to title

	def __str__(self):
		return self.title