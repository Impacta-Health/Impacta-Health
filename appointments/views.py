from django.shortcuts import render


def index(request):
    return render(request, "appointments/index.html")

def home(request):
    return render(request, "appointments/schedule.html")

def schedule(request):
    return render(request, "appointments/schedule.html")

def searchQueries(request):
    return render(request, "appointments/searchQueries.html")