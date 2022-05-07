from django import forms
from tempus_dominus.widgets import TimePicker

from .models import FixedContract, OccasionalContract, UserContractor


class USerContractForm(forms.ModelForm):
    # type_contractor = forms.ModelChoiceField(queryset=UserContractor.objects.all(), empty_label="ESCOJE UNA OPCION")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name_entity'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['extension'].widget.attrs.update({'class': 'form-control'})
        self.fields['nit'].widget.attrs.update({'class': 'form-control'})
        self.fields['type_contractor'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = UserContractor
        fields = ('name_entity', 'phone', 'extension', 'nit', 'type_contractor')


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class FixedContractForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contractor_by'].queryset = UserContractor.objects.filter(type_contractor='CONTRATANTE')
        self.fields['contractor_by'].widget.attrs.update({'class': 'form-control'})
        self.fields['contractor_for'].queryset = UserContractor.objects.filter(type_contractor='CONTRATISTA')
        self.fields['contractor_for'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control'})

    start_date = forms.DateField(widget=DatePickerInput)
    end_date = forms.DateField(widget=DatePickerInput)

    def clean_end_date(self):
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        if end_date < start_date:
            raise forms.ValidationError("La fecha final no puede ser menor a la Fecha Inicial")
        return end_date

    class Meta:
        model = FixedContract
        fields = ('contractor_by', 'contractor_for', 'start_date', 'end_date')



class OccasionalContractForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contractor_by'].widget.attrs.update({'class': 'form-control'})
        self.fields['nit'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['name_contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_contact'].widget.attrs.update({'class': 'form-control'})
        self.fields['destiny'].widget.attrs.update({'class': 'form-control'})
        self.fields['hour_service'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_service'].widget.attrs.update({'class': 'form-control'})
        self.fields['capacity'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_departure'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_arrival'].widget.attrs.update({'class': 'form-control'})
        self.fields['nro_spreadsheet'].widget.attrs.update({'class': 'form-control'})
        self.fields['reservation'].widget.attrs.update({'class': 'form-control'})
        self.fields['observations'].widget.attrs.update({'class': 'form-control'})

    date_service = forms.DateField(widget=DatePickerInput)
    destiny = forms.DateField(widget=DatePickerInput)
    date_departure = forms.DateField(widget=DatePickerInput)
    date_arrival = forms.DateField(widget=DatePickerInput)

    hour_service = forms.TimeField(
        widget=TimePicker(
            options={
                'defaultDate': '1970-01-01T14:56:00'
            },
            attrs={
                'input_toggle': True,
                'input_group': False,
            },
        ), )

    def clean_date_arrival(self):
        date_departure = self.cleaned_data['date_departure']
        date_arrival = self.cleaned_data['date_arrival']
        if date_arrival < date_departure:
            raise forms.ValidationError("La Fecha de llegada no puede ser menor a la de salida")
        return date_arrival

    class Meta:
        model = OccasionalContract
        fields = ('contractor_by', 'nit', 'address', 'city', 'name_contact',
                  'phone_contact', 'destiny', 'hour_service', 'date_service', 'capacity', 'date_departure',
                  'date_arrival', 'nro_spreadsheet', 'reservation', 'observations')
