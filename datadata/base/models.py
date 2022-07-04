import email
from unicodedata import name
from django.db import models

# Create your models here.

class Members(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class User(models.Model):
    firstname = models.CharField(max_length=200)
    secondname = models.CharField(max_length=200)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    password =models.CharField(max_length=200)
    password1 = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Car(models.Model):
    Driver_username = models.CharField(max_length=200)
    Vehicle_type = models.CharField(max_length=30)
    Number_plate = models.CharField(max_length=20)

    def __str__(self):
        return self.Number_plate

class Booking(models.Model):
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    CarBooked = models.ForeignKey(Car, on_delete=models.CASCADE)
    TimeDuration = models.CharField(max_length=200)
    TimeBooked = models.DateTimeField(auto_now_add=True)
    appointment = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.Username

User.objects.order_by("username")




