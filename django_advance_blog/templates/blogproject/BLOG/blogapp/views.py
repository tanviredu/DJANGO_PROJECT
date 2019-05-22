from django.shortcuts import render,get_object_or_404
from .models import Catagory,Post,Author
from django.http import HttpResponse
# Create your views here.

##give the home page
def home(request):
	return HttpResponse("home'")
	#return render(request,'home/home.html')



## find all the catagory
def catagory_list(request):
	catagories = Catagory.objects.all();
	context = {'catagories':catagories}
	return HttpResponse(catagories)
	#return render(request,'home/catagory_list.html')


## fine the post list with the catagory slug
def post_list(request,catagory_slug):

	##first fetch all the obj this is for different purpose
	catagories = Catagory.objects.all()

	## find the list of post based on the catagoery slug

	if catagory_slug:
		catagory = get_object_or_404(Catagory,slug=catagory_slug)  #find iif the catagory match
		## find all the Post on the catagory
		post = Post.objects.filter(catagory=catagory)

		context={'catagories':catagories,'catagory':catagory,'post':post}

	#return render(request,'home/post_list.html',context)
	return HttpResponse(post)

		## making context

def post_detail(request,slug,id):
	post = get_object_or_404(Post,slug=slug,id=id)
	## here slug is the catagory name

	context = {'post':post,'slug':slug}
	#return render(request,'home/detail.html',context)
	return HttpResponse(post)



def author_list(request):
	## firts fetch all the User
	post = Post.objects.all()

	context = {'post':post}

	return HttpResponse(post)
	#return render(request,'home/author.html',context)

def author_detail(request,slug):

	##first fetch all the obj this is for different purpose
	authors = Author.objects.all()

	## find the list of post based on the catagoery slug

	if slug:
		selected_author = get_object_or_404(Author,slug=slug)  #find iif the catagory match
		## find all the Post on the catagory
		#info = Author.objects.filter(catagory=catagory)

		#context={'catagories':catagories,'catagory':catagory,'post':post}

	#return render(request,'home/post_list.html',context)
	return HttpResponse(selected_author)