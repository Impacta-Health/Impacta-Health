from django.urls import path, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .views import PatientSignUpView, verify

app_name = 'users' 

urlpatterns = [
    path("patient/signup/", PatientSignUpView.as_view(), name="patient-signup"),
    path("signup/verify/", require_POST(csrf_exempt(verify)), name="signup-verify"),
]

