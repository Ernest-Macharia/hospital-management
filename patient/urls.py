from django.urls import path
from patient import views


urlpatterns = [

    path('', views.index, name="home"),
    path('register/', views.register, name="register"),
    path('', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),
    
    path('dashboard/', views.dashboard, name="dashboard"),
    path('admin/', views.admin, name='admin'),
    path('doctor/', views.doctor, name='doctor'),
    path('view_doctor/', views.view_doctor, name='view_doctor'),
    path('receptionist/', views.receptionist, name='receptionist'),
    path('view_patient/', views.view_patient, name='view_patient'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('recomendation_success/', views.recomendation_success, name='recomendation_success'),
    
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('view_appointment/', views.view_appointment, name='view_appointment'),
     path('view_recommendations/', views.view_recommendations, name='view_recommendations'),
      path('phamarcist/', views.phamarcist, name='phamarcist'),



]