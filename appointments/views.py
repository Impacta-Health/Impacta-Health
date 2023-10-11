from django.shortcuts import render, redirect
from django.utils import timezone
from appointments.forms import ScheduleForm
from django.views import View
from django.http import HttpResponse
from appointments.models import Appointment
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def index(request):
    return render(request, "appointments/index.html")


class CreateAppointmentView(View):
    template_name = 'appointments/schedule.html'
    form_class = ScheduleForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            return redirect('appointments:list')
        else:
            errors = form.errors.as_json()
            if errors:
                return HttpResponse(errors, status=400, content_type='application/json')
        return render(request, self.template_name, {"form": form})
    

@method_decorator(login_required(login_url='/users/login/'), name='dispatch')
class ListAppointmentsView(View):
    def get(self, request):
        appointments = None
        
        if request.user:
            appointments = Appointment.objects.filter(patient=request.user)
        
        context = {
            'appointments': appointments,
        }

        return render(request, 'appointments/appointments.html', context)



def reschedule(request):
    return render(request, "appointments/reschedule.html")




