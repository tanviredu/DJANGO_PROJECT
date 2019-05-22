# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from sklearn import *
import pickle
import numpy
# Create your views here.


def home(request):
    return render(request,'public/home.html');


def predict(request):
    return render(request,'public/predict.html')

def process(request):
    if request.method =='POST':
        slength = float(request.POST['slength'])
        swidth = float(request.POST['swidth'])
        plength = request.POST['plength']
        pwidth = request.POST['pwidth']
        filename = 'finalized_model.pickle'
        loaded_model = pickle.load(open(filename, 'rb'))
        prediction = loaded_model.predict([[slength, swidth, plength, pwidth]])
        ans = prediction[0];
        if ans==1:
            return render(request,'public/result.html',{'prediction': "Iris Setosa "})
        elif ans==2:
            return render(request,'public/result.html',{'prediction': "Iris Versicolour "})
        else:
            return render(request,'public/result.html',{'prediction': "Iris Virginica "})
        
        #return render(request,'public/result.html',{'prediction': prediction})



        ##return HttpResponse(pwidth);
        


    