from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['department', 'doctor', 'datetime']

    date = forms.DateField(widget=forms.DateInput(attrs={'id': 'datepicker'}))
    time = forms.TimeField(widget=forms.TextInput(attrs={'id': 'datepicker2'}))

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['department'].widget.attrs.update({'class': 'form-control'})
        self.fields['doctor'].widget.attrs.update({'class': 'form-control'})
