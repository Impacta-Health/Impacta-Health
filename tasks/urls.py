from django.urls import include, path

# Import views
from.import views

urlpatterns = [
   # path("ImpactaHealth/", views.ImpactaHealth),
    path("ImpactaHealth/", views.HtmlImpactaHealth, name="HtmlImpactaHealth"),
    path("ImpactaHealth/tasks/", views.home, name="home"),
]
