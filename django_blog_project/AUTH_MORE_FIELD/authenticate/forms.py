## we use the regular default form but that 
## form has a limitation it has only two fields
## so what we gonna do we extend that form so that 
## there will be more field and we can totally full fill the
## user database 
## and there is one more thing we need to understand
## we can only fill the fiend in the database that our
## User API provides
#So what exactly is metadata in case of a ModelForm?

#Any information that is “not a form Field” can be considered as metadata. Django provides sensible defaults to all fields. But if you want to override the default behavior of fields, you can define the corresponding meta options. Some meta options are compulsory.

#For example:

    #model: Model class to use for creating Form
   # fields: list to fields to include in the Form
  #  exclude: list of fields to exclude from the Form
 #   widgets: a dictionary of field-widget pairs

#And so on, there are many more meta options you can define inside Meta class.

from django.contrib.auth.forms import UserCreationForm,UserChangeForm
## so now we werk on the UserCreationForm here and extend it
## and the views.py will use it
from django.contrib.auth.models import User
## this is the database of the User that django create 
## now for the post
from .models import Post
from django import forms
## form creation API that we use
## we take the USercreation form
##add the field
## inside the meta class we define the database
## we gives all the filds that we create and also which will
## by default create


class editprofileform(UserChangeForm):

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password',)
	def __init__(self, *args, **kwargs):
		super(editprofileform,self).__init__(*args,**kwargs)
		self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Username'})
		self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email'})
		self.fields['password'].widget.attrs.update({'class':'form-control','placeholder':'Enter Password'})
		#self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Enter Password again'})
		self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':'Enter First Name'})
		self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':'Enter Last Name'})



class signupform(UserCreationForm):
	email = forms.EmailField(max_length=100)
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2')

	#here in the meta class we add the field that we write and also shows what we dont write
	def __init__(self, *args, **kwargs):
		super(signupform,self).__init__(*args,**kwargs)
		self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Username'})
		self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email'})
		self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Enter Password'})
		self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Enter Password again'})
		self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':'Enter First Name'})
		self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':'Enter Last Name'})


## this class is for posting blog
## we add the defauly post form from the form 


class Postform(forms.ModelForm):
	## nothing is needed because we use the default
	class Meta:
		## define the model again
		model = Post
		## now the field which is needed
		fields = ('title','text',)
	def __init__(self, *args, **kwargs):
		super(Postform,self).__init__(*args,**kwargs)
		self.fields['title'].widget.attrs.update({'class':'form-control','placeholder':'Enter Title'})
		self.fields['text'].widget.attrs.update({'class':'form-control','placeholder':'Content'})

