from django.shortcuts import render
from django.http import HttpResponse

## import the models and actually the Object
from .models import Post



def post_list(request):
	#return HttpResponse('hello')
	## find all the post
	posts = Post.objects.all().order_by('published_date');
	return HttpResponse(posts);
# Create your views here.
