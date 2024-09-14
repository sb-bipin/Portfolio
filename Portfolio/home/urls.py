
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.home,name='home'),
    path('education/', views.education, name='education'),
    path('experience/', views.experience, name='experience'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),
    path('resume/', views.resume, name='resume'),

]
