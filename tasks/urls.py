from django.urls import include, path

# Import views
from.import views

urlpatterns = [
   # path("ImpactaHealth/", views.ImpactaHealth),
    path("", views.HtmlImpactaHealth, name="HtmlImpactaHealth"),
    path("tasks/ConsultaExames.html", views.home, name="index"),
    path("tasks/ReagendarConsulta.html", views.Rconsultas, name="Rconsultas"),
    
]
