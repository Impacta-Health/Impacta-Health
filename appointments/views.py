from django.shortcuts import render


def index(request):
    return render(request, "appointments/index.html")

def home(request):
    return render(request, "appointments/schedule.html")

def reschedule(request):
    return render(request, "appointments/reschedule.html")