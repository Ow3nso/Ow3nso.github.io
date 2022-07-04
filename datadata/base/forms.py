from django.forms import ModelForm
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'appointment': DateInput(),
        }

class Newuser(ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class Loguser(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password1']
