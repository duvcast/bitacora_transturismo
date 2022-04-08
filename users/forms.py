from django import forms

from users.models import Manager


class ManagerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Manager
        fields = ('first_name', 'last_name',)
