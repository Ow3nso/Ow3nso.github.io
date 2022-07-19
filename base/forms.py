from dataclasses import fields
from django.forms import DateInput, ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth. models import User

class Patientform(ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

class Diagnosisform(ModelForm):
    class Meta:
        model = Diagnosisupdate
        fields = "__all__"

class DateInput(forms.DateInput):
    input_type = 'date'

class Bookform(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            'bookdate':DateInput(),
        }

class Registerform(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField(max_length=200)
    lastname = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'firstname','lastname','email','password1','password2')