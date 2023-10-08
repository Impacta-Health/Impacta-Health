from django.urls import include, path

# Import views
from.import views


app_name = "appointments"

urlpatterns = [
    path("", views.index, name="index"),
    path("appointments/schedule.html", views.home, name="schedule"),
    path("appointments/searchQueries.html", views.searchQueries, name="searchQueries"),
    path("appointments/schedule.html", views.schedule, name="schedule"),
    
]
