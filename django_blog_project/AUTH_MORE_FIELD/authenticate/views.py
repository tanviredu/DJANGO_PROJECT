from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages
from .forms import signupform,editprofileform
from django.utils import timezone
## django has built in form so that we can use it

from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
## user change form for changin the user
from .models import Post
from .forms import Postform



def index(request):
	return render(request,'authenticate/home.html',{})

def login_user(request):
	if request.method =='POST':
		## try to fetch data
		username = request.POST['username']
		password = request.POST['password']

		# ok now we get the data
		## lets authenticate it
		user = authenticate(request,username = username ,password=password)
		if user is None:
			messages.success(request,('problem using loggin in'))
			return redirect('login')
		else:
			login(request,user)  ## this will log you in the main django administration
			#to send a confirmation messages
			messages.success(request,('you have successfully loged in'))

			return redirect('index')
	else:
		return render(request,'authenticate/login.html',{})



## you cant create the login function 
## because there is a default function called login
def logout_user(request):
	logout(request)
	messages.success(request,("you are logged out"))
	return redirect('index')

def create_user(request):
	if request.method=='POST':
		## this create user is inherited from the UserCreatiion
		## that means we user some of the code of the 
		## user creation for
		## fill the form with ther data nad create a user object
		form = signupform(request.POST)
		#get the form data now check weather it is valif
		if form.is_valid():
			form.save()
			##now if the form is valid means he insert all the value
			#then we take the data from another method
			#we dont need to fetch the data from the login method way
			username = form.cleaned_data['username']
			password  = form.cleaned_data['password1']
			#now authnticate like the login
			user = authenticate(username=username,password=password)
			login(request,user)
			messages.success(request,('you have registered'))
			return redirect('index')
			## now the form has all the list of the data we
		## are posting 
		##as we know we need to passs the data as a dictionary form
		## we need to create a dictonary
		 
	else:
		## give and  empty result
		form = signupform()
	context = {'form':form}
	return render(request,'authenticate/register.html',context)


def edit_profile(request):
	if request.method=='POST':
		## this create user is inherited from the UserCreatiion
		## that means we user some of the code of the 
		## user creation for
		## fill the form with ther data nad create a user object
		form = editprofileform(request.POST,instance=request.user)
		## this is for whenever you ae trying to edit the user \
		## you have to give the current user object that you 
		## want to change
		## that means it gives you a form also but filled with all the
		## value of the user that you want to change

		#get the form data now check weather it is valif
		if form.is_valid():
			form.save()
			##now if the form is valid means he insert all the value
			#then we take the data from another method
			#we dont need to fetch the data from the login method way
			#username = form.cleaned_data['username']
			#password  = form.cleaned_data['password1']
			#now authnticate like the login
			#user = authenticate(username=username,password=password)
			#login(request,user)
			messages.success(request,('profile edited successfully...'))
			return redirect('index')
			## now the form has all the list of the data we
		## are posting 
		##as we know we need to passs the data as a dictionary form
		## we need to create a dictonary
		 
	else:
		## give and  empty result
		form = editprofileform(instance=request.user)
	context = {'form':form}
	return render(request,'authenticate/edit_profile.html',context)



def change_password(request):
	if request.method=='POST':
		
		form = PasswordChangeForm(data=request.POST,user=request.user)
		

		#get the form data now check weather it is valif
		if form.is_valid():
			form.save()
			messages.success(request,('Password Change successfully...'))
			return redirect('index')
		 
	else:
		## give and  empty result
		form = PasswordChangeForm(user=request.user)
	context = {'form':form}
	return render(request,'authenticate/change_password.html',context)


def blog(request):
	## before rendering the data we need to fetch data
	## from the database
	all_posts = Post.objects.all().order_by('-published_date')
	data = {'all_posts':all_posts}
	return render(request,'authenticate/blog.html',data)


def new_post(request):
	## check weather it is POST request
	if request.method =='POST':
		form = Postform(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			## need to suply this argument
			## it means dont save it yet 
			#other thing also needed
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			messages.success(request,('Successfully posted'))
			return redirect('index')
	else:
		form = Postform()
	return render(request,'authenticate/new_post.html',{'form':form})