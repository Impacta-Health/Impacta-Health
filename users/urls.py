from django.urls import path, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .views import PatientSignUpView, LoginView, custom_logout, signup_verify, login_verify

app_name = 'users' 

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path('logout/', custom_logout, name='logout'),
    path("login/verify/", require_POST(csrf_exempt(login_verify)), name="login-verify"),
    path("signup/verify/", require_POST(csrf_exempt(signup_verify)), name="signup-verify"),
    path("patient/signup/", PatientSignUpView.as_view(), name="patient-signup"),
]