from django import forms

from .models import Bus


class BusDriverForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['driver'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Bus
        fields = ('name', 'driver',)
