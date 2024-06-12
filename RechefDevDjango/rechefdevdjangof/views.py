from django.shortcuts import render
from django.http import HttpResponse

def django_install_success(request):
    return HttpResponse("Django installation worked successfully!")

def splash(request):
    return render(request, 'splash.html')
    #return HttpResponse('Hello World')
    
def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def fooddetails(request):
    return render(request, 'fooddetails.html')