from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.login,name='login'),
    path('register/',views.register,name='register'),
    path('processreg/',views.processreg,name='processreg'),
    path('processlogin/',views.processlogin,name='processlogin')

]
