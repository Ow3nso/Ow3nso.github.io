from django.db import models

# Create your models here.

class Gender(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Patient(models.Model):
    
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    contact = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    age = models.IntegerField()
    residence = models.CharField(max_length=200)
    kin = models.CharField(max_length=200)
    kincontacts = models.IntegerField()
    diagnosis = models.TextField()
    management = models.TextField()
    datejoin = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return (self.id)


class Diagnosisupdate(models.Model):
    patientid =  models.IntegerField(blank=True, null=True)
    diagnosis = models.TextField()
    management = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Status(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type
    

class Book(models.Model):
    patientid = models.IntegerField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True, default=1)
    bookdate = models.DateField()



