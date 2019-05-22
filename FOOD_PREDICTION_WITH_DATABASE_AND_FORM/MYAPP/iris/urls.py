
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('predict/',views.predict,name='predict'),
    path('inputiris/',views.inputiris,name='inputiris'),
    path('inputfood/',views.inputfood,name='inputfood'),
    path('inputiris/process/',views.inputiris_process,name='inputiris_process'),
]
