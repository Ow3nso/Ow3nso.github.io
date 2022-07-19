from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.home, name='home'),
    path('addpatients',views.addpatients, name='addpatients'),
    path('patients', views.patients, name='patients'),
    path('appointments', views.appointments, name='appointments'),
    path('showpatient/<patient_id>', views.showpatient, name='showpatient'),
    path('update/<book_id>', views.update_bookings, name='update'),
    path('delete/<book_id>', views.delete_bookings, name='delete'),
    path('bookpatient', views.book, name='bookpatient'),
    path("search", views.search, name="search"),
    path('diagnosis/<patient_id>', views.diagnosis, name='diagnosis'),
    path('login', views.loginpage, name='login'),
    path('register', views.register_user, name='register'),
    path('logout', views.logoutuser, name='logout'),
    path('archives',views.archives, name='archives')
]