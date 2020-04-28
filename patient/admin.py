from django.contrib import admin
from patient.models import Patient, Recommendations, Doctor, Appointment, Phamarcist, Receptionist
from patient.forms import SignUpForm, DoctorForm, ReceptionistForm, PatientForm, RecommendationForm, AppointmentForm, PhamarcistForm
# Register your models here.
class PatientAdmin(admin.ModelAdmin):
	list_display = ['location', 'Email','Phone', 'gender']
	form = PatientForm
	list_filter = ['Phone']
	search_fields = ['Phone']
class DoctorAdmin(admin.ModelAdmin):
	list_display = ['Name','Speciality','Phone', 'gender']
	form = DoctorForm
	list_filter = ['Speciality']
	search_fields = ['Speciality']
class PhamarcistAdmin(admin.ModelAdmin):
	list_display = ['Email','Phone', 'gender']
	form = PhamarcistForm
	list_filter = ['Phone']
class RecommendationsAdmin(admin.ModelAdmin):
	list_display = ['illness','patient']
	form = RecommendationForm
	list_filter = ['illness', 'patient']
	search_fields = ['illness', 'patient']
class AppointmentAdmin(admin.ModelAdmin):
	list_display = ['user','Doctor','Date', 'status']
	form = AppointmentForm
	list_filter = ['user','Doctor']
	search_fields = ['user','Doctor']
class ReceptionistAdmin(admin.ModelAdmin):
	list_display = ['Email','Phone', 'gender']
	form = DoctorForm
	list_filter = ['Phone']
	search_fields = ['Phone']

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Phamarcist,PhamarcistAdmin)
admin.site.register(Recommendations,RecommendationsAdmin)
admin.site.register(Appointment,AppointmentAdmin)
admin.site.register(Receptionist,ReceptionistAdmin)

