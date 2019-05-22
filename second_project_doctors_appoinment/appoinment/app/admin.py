from django.contrib import admin
from .models import Admin,Doctor,Department,Patient

class Catagoryadmin(admin.ModelAdmin):
    list_display = ['name','slug','title']
    prepopulated_fields = {'slug':('name',)}
    
    
class Catagorydoctor(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
    
class Catagorydepartment(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
    
class Catagorypatient(admin.ModelAdmin):
    list_display = ['name','department','time']
        
admin.site.register(Admin,Catagoryadmin)
admin.site.register(Doctor,Catagorydoctor)
admin.site.register(Patient,Catagorypatient)
admin.site.register(Department,Catagorydepartment)


