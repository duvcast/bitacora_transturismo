from django import forms
from tempus_dominus.widgets import TimePicker

from .models import Bus, ReliefDriver, Novelty, ReliefBus


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


class BusReliefForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bus'].widget.attrs.update({'class': 'form-control'})
        self.fields['relief'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control'})

    start_date = forms.DateField(widget=DatePickerInput)
    end_date = forms.DateField(widget=DatePickerInput)

    class Meta:
        model = ReliefBus
        fields = ('bus', 'relief', 'start_date', 'end_date')


class DriverReliefForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['driver'].widget.attrs.update({'class': 'form-control'})
        self.fields['relief'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control'})

    start_date = forms.DateField(widget=DatePickerInput)
    end_date = forms.DateField(widget=DatePickerInput)

    def clean_end_date(self):
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        if end_date < start_date:
            raise forms.ValidationError("La Fecha final no puede ser menor a la Inicial")
        return end_date

    class Meta:
        model = ReliefDriver

        fields = ('driver', 'relief', 'start_date', 'end_date')


class NoveltyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

    start_date = forms.DateField(widget=DatePickerInput)
    end_date = forms.DateField(widget=DatePickerInput)

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

    def clean_end_date(self):
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        if end_date < start_date:
            raise forms.ValidationError("La Fecha final no puede ser menor a la Inicial")
        return end_date

    class Meta:
        model = Novelty
        # TODO: this labels doesnt work
        labels = {
            'bus': 'Bus',
            'start_date': 'Fecha Inicio',
            'end_date': 'Fecha Final',
            'start_hour': 'Hora inicio',
            'end_hour': 'Hora Fin',
            'description': 'Descripcion',
        }
        fields = ('bus', 'start_date', 'end_date', 'start_hour', 'end_hour',
                  'description')


