from django.urls import include, path

# Import views
from.import views


app_name = "appointments"

urlpatterns = [
    path("", views.index, name="index"),
    path("appointments/schedule", views.CreateAppointmentView.as_view(), name="schedule"),
    path("appointments/list", views.ListAppointmentsView.as_view(), name="list"),
    path("appointments/reschedule.html", views.reschedule, name="reschedule"),
    
]
