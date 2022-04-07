from django import forms

from .models import FixedContract


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
