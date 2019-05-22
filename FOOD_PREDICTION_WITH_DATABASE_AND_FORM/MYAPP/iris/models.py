from django.db import models
import datetime
# Create your models here.

class Imformation(models.Model):
	name = models.CharField(max_length = 200)
	slength = models.FloatField()
	swidth = models.FloatField()
	plength = models.FloatField()
	pwidth = models.FloatField()
	result = models.CharField(max_length = 200)
	date = models.DateTimeField('Event Date')

	def __str__(self):
		return self.name
