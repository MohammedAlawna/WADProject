from django.shortcuts import redirect,render
from WAD.forms import LogForm
from WAD.models import LogMessage
import json
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#def login(request):
#    return render(request, 'login.html')

def pricing(request):
    return render(request, 'pricing.html')

def staff(request):
    return render(request, 'staff.html')

def contact(request):
    return render(request, 'contact.html')

def showPlans(request):
    plans = LogMessage.objects.order_by("-log_date")
    return render(request, "ShowSubs.html", {"plans_list": plans})

def addPlan(request):
    form = LogForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        plan = form.save(commit=False)
        plan.log_date = datetime.now()
        plan.save()
        return redirect("show")

    else:
        return render(request, "OrderSubs.html", {"form": form})