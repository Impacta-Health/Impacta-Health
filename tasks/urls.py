from django.urls import include, path

# Import views
from.import views

urlpatterns = [
   # path("ImpactaHealth/", views.ImpactaHealth),
    path("", views.HtmlImpactaHealth, name="HtmlImpactaHealth"),
    
]
