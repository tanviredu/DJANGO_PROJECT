from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.
from .models import Tutorial


def index(request):
    data = Tutorial.objects.all
    return render(request,'main/home.html',{'tutorials':data})


def login(request):
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
        else:
            return HttpResponse('problem registering')
    else:
        return HttpResponse('problem registering')


def processlogin(request):
    if request.method=='POST':
        username1 = request.POST['username1']
        password1 = request.POST['password1']
        user = authenticate(request,username=username1,password=password1)
        if user is not None:
            return redirect(index)
        else:
            return HttpResponse('<h1>Wrong credential</h1>')
        
def postlist(request):
    #return HttpResponse('hello')
    post_list = Tutorial.objects.all
    
    return render(request,'main/post_list.html',{'tutorials':post_list})

def postdetail(request,pk):
    #return HttpResponse(pk)
    data = Tutorial.objects.get(pk=pk)
    return render(request,'main/one_post.html',{'tutorials':data})
    ##return HttpResponse(data.content)
    ## if you want to query with
    ## the primary key it will not be iterable


### this is how you deal with the link
### first make the urlpattern
##like /process/<int:pk>
## then in the link just /process/{{value.pk}} and only the value will be
## inside a bracet not the whole

def search(request):
    ##return HttpResponse('hello')
    query = request.POST['q']
    ## now we have to query
    #result = [] ## we store the info there
    if query:
        results = Tutorial.objects.filter(content__contains = query)
        return render_to_response('main/search.html',{'query':query,'results':results})

    ##return HttpResponse(query)

 