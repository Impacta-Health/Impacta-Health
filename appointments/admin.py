from django.contrib import admin
from appointments.models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'department', 'doctor', 'datetime', 'created_at', 'updated_at')
    list_filter = ('department', 'doctor', 'datetime')
    search_fields = ('patient__username', 'doctor', 'datetime')


admin.site.register(Appointment, AppointmentAdmin)