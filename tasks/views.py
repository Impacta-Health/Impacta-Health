from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

#def ImpactaHealth(request):
 #   return HttpResponse("Meu Projeto")

def HtmlImpactaHealth(request):
    return render(request, "tasks/ImpactaHealth.html")

def home(request):
    return render(request, "tasks/index.html")