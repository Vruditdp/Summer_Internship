import mysql.connector
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    return render(request,'login.html')
    
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def authentication(request):
    uname = request.POST["uname"]
    passwd = request.POST["pass"] 

    if ((uname=='bunty' and passwd=='123') or (uname=='vrudit' and passwd=='321')):
        return render(request,'display.html',{'uname':uname})
    else:
        return render(request,'login.html')    
