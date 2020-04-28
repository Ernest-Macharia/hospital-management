from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime
from model_utils import Choices
from django.utils import timezone

	


class Doctor(models.Model):
    gender_choice = Choices('SELECT','male','female')
    speciality_choice = Choices('SELECT','Surgeon','Dentist','Orthopaedic','Optician','General Doctor','Gynacologist')
    Name = models.CharField(max_length=100, default=None)
    Speciality = models.CharField(max_length=100 ,choices=speciality_choice, default=speciality_choice.SELECT)
    Address = models.CharField(max_length=100 , default=None)
    Email = models.CharField(max_length=100 , default=None)
    Phone = models.CharField(max_length=100 , default=None)
    gender = models.CharField(max_length=100 , choices=gender_choice,default=gender_choice.SELECT)

    def __str__(self):
        return self.Name
class Phamarcist(models.Model):
    gender_choice = Choices('SELECT','male','female')
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100 , default=None)
    Email = models.CharField(max_length=100 , default=None)
    Phone = models.CharField(max_length=100 , default=None)
    gender = models.CharField(max_length=100 , choices=gender_choice,default=gender_choice.SELECT)

    def __str__(self):
        return self.Name



class Receptionist(models.Model):
    gender_choice = Choices('SELECT','male','female')
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100 , default=None)
    Email = models.CharField(max_length=100 , default=None)
    Phone = models.CharField(max_length=100 , default=None)
    gender = models.CharField(max_length=100 , choices=gender_choice,default=gender_choice.SELECT)

    def __str__(self):
        return self.Name


class Patient(models.Model):
    gender_choice = Choices('SELECT','male','female')
    Name = models.CharField(max_length=100)
    location = models.CharField(max_length=500 , blank=True , default='')
    
    Address = models.CharField(max_length=100 , default=None)
    Email = models.CharField(max_length=100 , default=None)
    Phone = models.CharField(max_length=100 , default=None)
    gender = models.CharField(max_length=100 , choices=gender_choice,default=gender_choice.SELECT)

    def __str__(self):
        return self.Name
class Recommendations(models.Model):
	medicine_choice = Choices('SELECT','asprin','amoxil','piriton','brufen','panadol','paracitamol')
	illness = models.TextField()

	medicine = models.CharField(max_length=100,choices=medicine_choice,
                              default=medicine_choice.SELECT)
	patient = models.ForeignKey(Patient,null=True, on_delete=models.CASCADE)

    

    


class Appointment(models.Model):
    user = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(Doctor , default=None, on_delete=models.CASCADE)
    Date = models.DateField(default=timezone.now)
    status_choice = Choices('SELECT','Pending','Approved','Not Approved')
    status = models.CharField(max_length=20,choices=status_choice,default=status_choice.SELECT)

    message = models.CharField(max_length=1000 , default="Pending Approval")
    

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('index')
