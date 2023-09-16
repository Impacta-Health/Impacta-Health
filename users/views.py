from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from users.forms import AdminSignUpForm, DoctorSignUpForm, PatientSignUpForm
from users.models.user_model import AdminUser, DoctorUser, PatientUser, User
from users.validators.username_validator import validate_username

class SignUpView(View):
    user_model = None

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                username = form.cleaned_data["username"]
                first_name = form.cleaned_data["first_name"]
                last_name = form.cleaned_data["last_name"]
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password2"]

                self.user_model.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                )
                return redirect('appointments:index')
            else:
                errors = form.errors.as_json()
                if errors:
                    return HttpResponse(errors, status=400, content_type='application/json')
        return render(request, self.template_name, {"form": form})

class PatientSignUpView(SignUpView):
    user_model = PatientUser
    template_name = "patient_signup.html"
    form_class = PatientSignUpForm


class AdminSignUpView(SignUpView):
    user_model = AdminUser
    template_name = "admin_signup.html"
    form_class = AdminSignUpForm


class DoctorSignUpView(SignUpView):
    user_model = DoctorUser
    template_name = "doctor_signup.html"
    form_class = DoctorSignUpForm


@require_POST
@csrf_exempt
def verify(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    
    username_exists = False  # Inicialmente, definimos como falso
    email_exists = User.objects.filter(email=email).exists()

    username_error = ''
    
    if username is not None and username.strip():  # Verifica se o campo de nome de usuário não é None e não está vazio
        try:
            validate_username(username)
            username_exists = User.objects.filter(username=username).exists()
        except ValidationError as e:
            username_error = e.messages[0] if e.messages else ''

    data = {'username_exists': username_exists, 'email_exists': email_exists, 'username_error': username_error}
    return JsonResponse(data)