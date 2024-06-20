from django.shortcuts import render
from django.http import HttpResponse

def django_install_success(request):
    return HttpResponse("Django installation worked successfully!")

def splash(request):
    return render(request, 'splash.html')
    #return HttpResponse('Hello World')
    
def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def home_pt(request):
    return render(request, 'home-pt.html')

def home_lp(request):
    return render(request, 'home-lp.html')

def fooddetails(request):
    return render(request, 'food-details.html')

def scan(request):
    return render(request, 'scan.html')
