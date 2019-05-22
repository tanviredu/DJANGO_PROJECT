from django.db import models

# Create your models here.

class Tutorial(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    published = models.DateTimeField('date published')

    def __str__(self):
        return self.title

