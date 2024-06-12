from django.urls import path
from . import views

urlpatterns = [
    #path('/', views.django_install_success),
    path('', views.splash, name='splash'), 
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('fooddetails/', views.fooddetails, name='fooddetails')
]