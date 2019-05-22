from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages

## django has built in form so that we can use it

from django.contrib.auth.forms import UserCreationForm
# Create your views here.




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
		form = UserCreationForm(request.POST)
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
		form = UserCreationForm()
	context = {'form':form}
	return render(request,'authenticate/register.html',context)