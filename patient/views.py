from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from patient.forms import SignUpForm, DoctorForm, ReceptionistForm, PatientForm, RecommendationForm, AppointmentForm, PhamarcistForm
from django.contrib.auth.decorators import login_required
import copy
from .models import  Appointment , Patient , Doctor, Receptionist, Recommendations

# Create your views here.


def index(request):
    return render(request, 'index.html')

def register(request):

    form = SignUpForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():

            form.save()

            username = form.cleaned_data.get('username')

            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)

            login(request, user)

            return redirect('login')
    else:

        form = SignUpForm()

    return render(request, 'registration/register.html', {'form': form})


def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render('dashboard')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(
                username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'registration/login.html', {})

@login_required
def userLogout(request):
    logout(request)
    return render('login')


@login_required
def admin(request):
    return redirect(admin.site.urls)


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def doctor(request):
    return render(request, 'doctor.html')


def view_doctor(request):
    context = {"view_doctor": Doctor.objects.all()}
    return render(request, "doctor_list.html", context)



def recommendations(request):
    if request.method == "GET":
        form = RecommendationForm()
        return render(request, "recommendation.html", {'form': form})
    else:
        form = RecommendationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/recomendation_success")
def recomendation_success(request):
    return render(request, 'recommendation_success.html')

def view_recommendations(request):
    context = {'view_recommendations': Recommendations.objects.all()}
    return render(request, "recommendation_list.html", context)


def receptionist(request):
    return render(request, 'receptionist.html')





def add_patient(request):
    if request.method == "GET":
        form = PatientForm()
        return render(request, "patient_registration.html", {'form': form})
    else:
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/receptionist")

def view_patient(request):
    context = {"view_patient": Patient.objects.all()}
    return render(request, "patient_list.html", context)

def add_appointment(request):
    if request.method == "GET":
        form = AppointmentForm()
        return render(request, "appointment.html", {'form': form})
    else:
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/receptionist")
def view_appointment(request):
    context = {"view_appointment": Appointment.objects.all()}
    return render(request, "appointment_list.html", context)

def phamarcist(request):
    return render(request, 'phamarcist.html')



