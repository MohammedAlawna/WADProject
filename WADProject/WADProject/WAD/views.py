from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def pricing(request):
    return render(request, 'pricing.html')

def staff(request):
    return render(request, 'staff.html')

def contact(request):
    return render(request, 'contact.html')