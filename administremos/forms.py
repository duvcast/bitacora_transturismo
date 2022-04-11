from django import forms
from tempus_dominus.widgets import TimePicker

from .models import Bus, Novelty


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class BusDriverForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['driver'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Bus
        fields = ('name', 'driver',)


class NoveltyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bus'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_hour'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_hour'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})

    start_date = forms.DateField(widget=DatePickerInput)
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
    end_date = forms.DateField(widget=DatePickerInput)
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

    class Meta:
        model = Novelty
        fields = ('bus', 'start_date', 'start_hour', 'end_date', 'end_hour', 'description')
