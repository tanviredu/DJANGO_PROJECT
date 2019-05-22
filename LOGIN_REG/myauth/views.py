from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect

# Create your views here.

def login(request):
    #return HttpResponse('hello')
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')

def processreg(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = str(fname)+str(lname)
        email = request.POST['email']
        password = request.POST['password']
        password_re = request.POST['repassword']

        if username and email and password:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('login')
            ## redirect parameter takes the function name

            #return HttpResponse('success')
        return HttpResponse('failure')
    else:
        return HttpResponse('POST Problem')
        


def processlogin(request):
    if request.method=='POST':
        username = request.POST['username1']
        password = request.POST['password1']
    #    return HttpResponse(username)
        if username and password:
            #return HttpResponse(username)
            user = authenticate(username=username,password=password)
    #        return HttpResponse(user)
            if user:
                return HttpResponse('logged in')
            else:
                return HttpResponse('you are not the user')
        else:
            return HttpResponse('problem')
    else:
        return HttpResponse('problem')