from django import forms

from .models import Contract


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class ContractForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_contract'].widget.attrs.update({'class': 'form-control'})
        self.fields['number_contract'].widget.attrs.update({'class': 'form-control'})
        self.fields['contractor_by'].widget.attrs.update({'class': 'form-control'})
        self.fields['contractor_for'].widget.attrs.update({'class': 'form-control'})
        self.fields['type_contract'].widget.attrs.update({'class': 'form-control'})
        self.fields['arrival'].widget.attrs.update({'class': 'form-control'})
        self.fields['departure'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control'})

    start_date = forms.DateField(widget=DatePickerInput)
    end_date = forms.DateField(widget=DatePickerInput)

    class Meta:
        model = Contract
        fields = (
            'number_contract', 'type_contract', 'contractor_by', 'contractor_for', 'start_date', 'end_date', 'arrival',
            'departure')


class UpdateContractForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_contract'].widget.attrs.update({'class': 'form-control'})
        self.fields['number_contract'].widget.attrs.update({'class': 'form-control'})
        self.fields['contractor_by'].widget.attrs.update({'class': 'form-control'})
        self.fields['contractor_for'].widget.attrs.update({'class': 'form-control'})
        self.fields['type_contract'].widget.attrs.update({'class': 'form-control'})
        self.fields['arrival'].widget.attrs.update({'class': 'form-control'})
        self.fields['departure'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control'})

    start_date = forms.DateField(widget=DatePickerInput)
    end_date = forms.DateField(widget=DatePickerInput)

    class Meta:
        model = Contract
        fields = (
            'number_contract', 'type_contract', 'contractor_by', 'contractor_for', 'start_date', 'end_date', 'arrival',
            'departure')
