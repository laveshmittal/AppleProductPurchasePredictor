from django.shortcuts import render, redirect
from .model import *
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import array
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create your views here.

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

mod = MlModel()


def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'dashboard.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def predictfunc(request):
    return render(request, "predictfunc.html")


def app1homepage(request):

    return render(request, 'app1homepage.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def predictcount(request):

    gender = request.GET.get("gender", "")
    age = request.GET.get("age", "")
    salary = request.GET.get("salary", "")
    if gender is 'Male':
        gender = 1
    else:
        gender = 0
    age = int(age)
    salary = int(salary)
    resultDict = mod.predict([gender, age, salary])
    print(resultDict)
    if resultDict['knn'] == 0:
        result = "According to our KNN model, Uh-Oh! Our system predicts that user will not make this purchase "
    else:
        result = "According to our KNN model, Hooray! Our system predicts that user will buy this product"
    if resultDict['nb'] == 0:
        result1 = "According to our Naive Bayesian model, Uh-Oh! Our system predicts that user will not make this purchase "
    else:
        result1 = "According to our Naive Bayesian model, Hooray! Our system predicts that user will buy this product"

    passdict = {'knn': str(result), 'nb': str(
        result1), 'knnAccuracy': resultDict['knnAccuracy'], 'nbAccuracy': resultDict['nbAccuracy']}

    return render(request, 'predict.html',
                  passdict
                  )
