from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.urls import path
#from django.urls import path,include
urlpatterns = [
    path('', views.home,name="home"),
    path('predict/', views.predict,name="predict"),
    path('process/', views.process,name="process"),

]
