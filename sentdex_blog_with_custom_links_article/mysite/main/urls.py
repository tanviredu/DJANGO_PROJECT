from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/', views.login,name='login'),
    path('register/',views.register,name='register'),
    path('processreg/',views.processreg,name='processreg'),
    path('processlogin/',views.processlogin,name='processlogin'),
    path('postlist/',views.postlist,name='postlist'),
    path('postlist/postdetail/<int:pk>',views.postdetail,name='postdetail'),
    path('search/',views.search,name='search'),
]
