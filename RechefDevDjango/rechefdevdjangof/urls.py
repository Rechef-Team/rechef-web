from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'), 
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/pt/', views.home_pt, name='home-pt'),
    path('home/lp/', views.home_lp, name='home-lp'),
    path('scan/', views.scan, name='scan'),
    path('details/', views.fooddetails, name='food-details'),
]
