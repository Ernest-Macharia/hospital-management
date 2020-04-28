from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError
from .models import  Appointment , Patient , Doctor, Receptionist, Recommendations, Phamarcist

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
            'email': None,
            'password2': None,
            'password1': None
        }

    def clean_email(self):

        email = self.cleaned_data['email']

        if not email.endswith('@gmail.com') and not email.endswith('@yahoo.com') and not email.endswith('@outlook.com'):

            raise ValidationError('Domain of email is not valid')

        return email

    def clean_first_name(self):

        first = self.cleaned_data['first_name']

        print(first.isalpha())

        if not first.isalpha():
            raise ValidationError('Name cannot be numeric')

        return first

    def clean_second_name(self):

        first = self.cleaned_data['last_name']

        print(first.isalpha())

        if not first.isalpha():
            raise ValidationError('Name cannot be numeric')


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('Name','Address', 'Email', 'Phone', 'gender', 'Speciality')
class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendations
        fields = ('illness', 'medicine','patient')
class ReceptionistForm(forms.ModelForm):
    class Meta:
        model = Receptionist
        fields = ('Name','Address', 'Email', 'Phone', 'gender')
class PhamarcistForm(forms.ModelForm):
    class Meta:
        model = Phamarcist
        fields = ('Name','Address', 'Email', 'Phone', 'gender')
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('user','Doctor', 'Date', 'status', 'message')
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('Name', 'location','Address', 'Email', 'Phone', 'gender')