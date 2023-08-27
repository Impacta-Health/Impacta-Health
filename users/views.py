from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from users.forms import AdminSignUpForm, DoctorSignUpForm, PatientSignUpForm
from users.models.user_model import AdminUser, DoctorUser, PatientUser, User


class SignUpView(View):
    user_model = None

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
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

            success_message = "User successfully registered."
            return render(request, self.template_name, {"form": form, "success_message": success_message})
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
    user_model = AdminUser
    template_name = "doctor_signup.html"
    form_class = DoctorSignUpForm


@require_POST
@csrf_exempt
def verify(request):
    username = request.POST.get("username")
    exists = User.objects.filter(username=username).exists()
    return JsonResponse({"exists": exists})
