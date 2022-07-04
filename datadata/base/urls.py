from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.CreateBookings, name='form'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('navbar', views.navbar, name='navbar'),

]