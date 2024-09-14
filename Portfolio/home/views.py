from warnings import filters
from django.http import FileResponse, HttpResponseNotFound
from django.shortcuts import render,HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def home(request):
    return render(request,'home.html')
    # return HttpResponse("this is a homepage")


def education(request):
    return render(request, 'education.html')

def experience(request):
    return render(request, 'experience.html')

def skills(request):
    return render(request, 'skills.html')

def contact(request):
    return render(request, 'contact.html')
    

def resume(request):
    file_path = staticfiles_storage.path('resumenew.pdf')
    if file_path:
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    else:
        return HttpResponseNotFound('The requested file was not found.')    


