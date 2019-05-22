
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
	path('catagory_list/',views.catagory_list,name='catagory_list'),
	path('post_list/<str:catagory_slug>',views.post_list,name='post_list'),
	path('post_detail/<str:slug>/<int:id>',views.post_detail,name='post_detail'),
	path('author_list/',views.author_list,name='author_list'),
	path('author_detail/<int:slug>',views.author_detail,name='author_detail'),

		

]
