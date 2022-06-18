from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def homepage(request):
    return HttpResponse('home')

def about(request):
    return HttpResponse('about')

def login(request):
    return HttpResponse('login');

def loginMain(request, name):
    return render(request, 'loginOrig.html', 
                  {'name': name, 'date': datetime.now()})