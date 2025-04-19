from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    # return  HttpResponse('<h1>Hello World!!!!!!!!!!!!!</h1>')
    return render(request,"home.html",{'name':'Miniax'})


def add(request):
    # num1 = int(request.GET['num1'])
    # num2 = int(request.GET['num2'])

    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])

    result = num1 + num2
    return render(request,"result.html",{'result':result})

