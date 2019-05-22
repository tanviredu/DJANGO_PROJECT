from django.contrib import admin
from .models import Catagory,Post,Author 
#from django.contrib.auth.models import User

class Catagoryadmin(admin.ModelAdmin):
	list_display = ['name','slug']
	prepopulated_fields = {'slug':('name',)}

class Authoradmin(admin.ModelAdmin):
	list_display = ['name','slug']
	prepopulated_fields = {'slug':('name',)}


admin.site.register(Catagory,Catagoryadmin)
admin.site.register(Author,Authoradmin)

admin.site.register(Post)
