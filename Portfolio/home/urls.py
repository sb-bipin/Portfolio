
# from django.contrib import admin
# from django.urls import path
# from home import views

# urlpatterns = [
#     path("",views.home,name='home'),
#     path('education/', views.education, name='education'),
#     path('experience/', views.experience, name='experience'),
#     path('skills/', views.skills, name='skills'),
#     path('contact/', views.contact, name='contact'),
#     path('resume/', views.resume, name='resume'),

# ]


from django.contrib import admin
from django_distill import distill_path
from home import views

# helper function (no parameters needed for these views)
def get_none():
    return None

urlpatterns = [
    distill_path("", views.home, name='home', distill_func=get_none),
    distill_path("education/", views.education, name='education', distill_func=get_none),
    distill_path("experience/", views.experience, name='experience', distill_func=get_none),
    distill_path("skills/", views.skills, name='skills', distill_func=get_none),
    distill_path("contact/", views.contact, name='contact', distill_func=get_none),
    distill_path("resume/", views.resume, name='resume', distill_func=get_none),
]

