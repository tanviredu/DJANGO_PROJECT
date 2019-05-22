from django.shortcuts import render
from django.http import HttpResponse
from .models import Imformation
from sklearn import *
import pickle
import numpy
import datetime
# Create your views here.


def index(request):
	return render(request,'public/index.html')


def predict(request):
	return render(request,'public/predict.html')


def inputiris(request):
	return render(request,'public/iris.html')

def inputfood(request):
	return render(request,'public/food.html')


def find_ans(ans):
	if ans==1:
		res ="Iris Setosa";
	elif ans==2:
		res = "Iris Versicolour";
	else:
		res = "Iris Virginica"

	return res


def inputiris_process(request):
	if request.method== 'POST':
		try:
			username = request.POST['username']
			sslength  = float(request.POST['slength'])
			sswidth   = float(request.POST['swidth'])
			pplength  = float(request.POST['plength'])
			ppwidth   = float(request.POST['pwidth'])
			filename = 'finalized_model.pickle'
			loaded_model = pickle.load(open(filename, 'rb'))
			prediction = loaded_model.predict([[sslength, sswidth, pplength, ppwidth]])
			ans = prediction[0];
			res = find_ans(ans)
			data = Imformation(name=username,slength=sslength,swidth=sswidth,plength=pplength,pwidth=ppwidth,result=res,date=datetime.datetime.now())
			data.save()
			return render(request,'public/result.html',{'res':res});
		except:
			return HttpResponse("you are a looser")


