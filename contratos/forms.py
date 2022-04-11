from django import forms
from tempus_dominus.widgets import TimePicker

from .models import FixedContract, OccasionalContract, UserContractor


class USerContractForm(forms.ModelForm):
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
        self.fields['contractor_by'].widget.attrs.update({'class': 'form-control'})
        self.fields['contractor_for'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control'})

    start_date = forms.DateField(widget=DatePickerInput)
    end_date = forms.DateField(widget=DatePickerInput)

    class Meta:
        model = FixedContract
        fields = ('contractor_by', 'contractor_for', 'start_date', 'end_date')


class FixedContractEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contractor_by'].widget.attrs.update({'class': 'form-control'})
        self.fields['contractor_for'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = FixedContract
        fields = ('contractor_by', 'contractor_for',)


class OccasionalContractForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contractor_by'].widget.attrs.update({'class': 'form-control'})
        self.fields['nit'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_person'].widget.attrs.update({'class': 'form-control'})
        self.fields['contact_phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['arrival'].widget.attrs.update({'class': 'form-control'})
        self.fields['hour'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_service'].widget.attrs.update({'class': 'form-control'})
        self.fields['capacity'].widget.attrs.update({'class': 'form-control'})
        self.fields['go'].widget.attrs.update({'class': 'form-control'})
        self.fields['come_bak'].widget.attrs.update({'class': 'form-control'})
        self.fields['nro_spreadsheet'].widget.attrs.update({'class': 'form-control'})
        self.fields['reservation'].widget.attrs.update({'class': 'form-control'})
        self.fields['observations'].widget.attrs.update({'class': 'form-control'})
        self.fields['manager'].widget.attrs.update({'class': 'form-control'})

    date_service = forms.DateField(widget=DatePickerInput)
    hour = forms.TimeField(
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
        model = OccasionalContract
        fields = ('contractor_by', 'nit', 'address', 'city', 'contact_person',
                  'contact_phone', 'arrival', 'hour', 'date_service', 'capacity', 'go',
                  'come_bak', 'nro_spreadsheet', 'reservation', 'observations', 'observations', 'manager')
