from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

#Utiliar JWT PARA auth

class Patients(models.Model):

    sex_choices = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]


    nutrioligist = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    cellphone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, unique=True)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=sex_choices)

    def save(self):
        self.firstname = self.firstname.upper()
        self.lastname = self.lastname.upper()
        return super().save()


    #Crear metodo para normalizar Campos en busqueda de query
    def __str__(self):

        return '%s %s' % (self.firstname, self.lastname)


class PatientStats(models.Model):

    patient_name = models.ForeignKey(Patients, on_delete = models.CASCADE, related_name="patient")
    weight = models.FloatField()
    hip = models.FloatField()
    foreams = models.FloatField()
    date = models.DateField(default=datetime.date.today() )

class MealsPlan(models.Model):

    meals_file = models.FileField()
    date = models.DateField(default=datetime.date.today() )

class Appointment(models.Model):
    patient_name = models.ForeignKey(Patients, on_delete=models.CASCADE)
    nutriologist = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50, null=True)
    date_start = models.DateTimeField(null=True)
    date_end = models.DateTimeField(null=True)
    #start_hour = models.TimeField(null=True)
    #end_time = models.TimeField(null=True)
    place = models.TextField(null=True)
    description = models.TextField(null=True)


    def __str__(self):

        return '%s' % (self.patient_name)
