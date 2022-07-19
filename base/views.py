from ast import If
from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .forms import *
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

@login_required(login_url='login')
def home(request):

    patients = Patient.objects.all()

    bookings = Book.objects.all()

    total_patients = patients.count()

    total_bookings = bookings.count()

    context = {'total_patients':total_patients, 'total_bookings':total_bookings}

    return render(request, 'home.html', context)


@login_required
def patients(request):

    form = Diagnosisform

    patients = Patient.objects.all().order_by('firstname')

    context = {'patients':patients, 'form':form}

    return render(request, 'patients.html', context)

@login_required
def appointments(request):
    form = Bookform
    bookings = Book.objects.all().order_by('bookdate')

    patients = Patient.objects.all()

    context = {'bookings':bookings,'patients':patients}

    return render(request, 'appointments.html', context)


@login_required
def addpatients(request):

    form = Patientform

    if request.method=="POST":
        form = Patientform(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, ('New Patient added successfully'))
            return redirect('/')

    context = {'form':form}

    return render(request, 'addpatients.html', context)


@login_required
def showpatient(request, patient_id):

    diagnosis = Diagnosisupdate.objects.all()

    pat = Patient.objects.all()

    patients = Patient.objects.get(pk=patient_id)

    context = {'patients':patients, 'diagnosis':diagnosis, 'pat':pat}

    return render(request, 'show.html', context)

@login_required
def book(request):

    model = Book

    form = Bookform

    if request.method=="POST":
        form = Bookform(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, ('Appointment added successfully'))
            return redirect('/')

    context = {'form':form}
    return render(request, 'book.html', context)

@login_required
def search(request):

    if request.method =="POST":
        searched = request.POST['searched']
        patients = Patient.objects.filter(surname__contains=searched)

        context = {'searched':searched, 'patients':patients}

        return render(request, 'patients.html', context)

@login_required
def diagnosis(request, patient_id):

    patients = Patient.objects.get(pk=patient_id)

    form = Diagnosisform

    if request.method=="POST":
        form = Diagnosisform(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, ('Diagnosis added successfully'))
            return redirect('/')

    context = {'form':form}

    return render(request, 'adddiagnosis.html', context)

def loginpage(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Invalid username or password"))
            return redirect('login')

    else:

        return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('login')

def delete_bookings(request, book_id):
    
    book = Book.objects.get(pk=book_id)

    book.delete()

    return redirect('appointments')

def update_bookings(request, book_id):

    book = Book.objects.get(pk=book_id)

    form = Bookform(request.POST or None, instance=book)

    if request.method == "POST":
        if form.is_valid:
            form.save()
            return redirect('appointments')

    context = {'book':book, 'form':form}

    return render(request, 'update.html', context)

def archives(request):

    patients = Patient.objects.all()
    bookings = Book.objects.all().order_by('bookdate')

    context = {'bookings':bookings, 'patients':patients}

    return render(request, 'archives.html', context)


def register_user(request):

    form = Registerform

    if request.method=="POST":
        form = Registerform(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, firstname=firstname, lastname=lastname, email=email, password=password,)
            login(request, user)
            messages.success(request, ("Registration successful. Please Login"))
            return redirect('login')

    else:
        form = Registerform()


    context = {'form':form}

    return render(request, 'register.html', context)