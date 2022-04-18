from django import forms
from tempus_dominus.widgets import TimePicker

from .models import Service, Schedule


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class ServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['route_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control'})

    start_date = forms.DateField(widget=DatePickerInput)
    end_date = forms.DateField(widget=DatePickerInput)

    def clean_end_date(self):
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        if end_date < start_date:
            raise forms.ValidationError("La fecha final no puede ser menor a la inicial")
        return end_date

    class Meta:
        model = Service
        fields = ('route_name', 'start_date', 'end_date',)


class ScheduleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['type_schedule'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_hour'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_hour'].widget.attrs.update({'class': 'form-control'})
        self.fields['bus'].widget.attrs.update({'class': 'form-control'})

    start_hour = forms.TimeField(
        widget=TimePicker(
            options={
                'defaultDate': '1970-01-01T14:56:00'
            },
            attrs={
                'input_toggle': True,
                'input_group': False,
            },
        ), )
    end_hour = forms.TimeField(
        widget=TimePicker(
            options={
                'defaultDate': '1970-01-01T14:56:00'
            },
            attrs={
                'input_toggle': True,
                'input_group': False,
            },
        ), )

    def clean_end_hour(self):
        start_hour = self.cleaned_data['start_hour']
        end_hour = self.cleaned_data['end_hour']
        if end_hour < start_hour:
            raise forms.ValidationError("La Hora final no puede ser menor a la inicial")
        return end_hour

    class Meta:
        model = Schedule
        fields = ('type_schedule', 'start_hour', 'end_hour', 'bus')
