from atexit import register
from dataclasses import fields
from email.message import Message
from multiprocessing import context
from pyexpat import model
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User, auth


from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import *


# Create your views here.

def home(request):
    bookings = Booking.objects.all()

    return render(request, 'home.html', {'bookings' : bookings} )

def CreateBookings(request):
    model = Booking

    form = BookingForm

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Bookings Made Successfully.')
            return redirect('/')


    return render(request, 'add.html', {'form':form})

def registerPage(request):

    form = Newuser

    if request.method == 'POST':
        form = Newuser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created Successfully. Please Log in')
            return redirect('login')


    context = {'form':form}
    return render(request, 'register.html', context)
    

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        
    context = {}
    return render(request, 'login.html', context)


def navbar(request):
    return render(request, 'navbar.html')