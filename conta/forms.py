from django import forms
from crum import get_current_user
from .models import Conta


class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta

        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContaForm, self).__init__(*args, **kwargs)
        self.initial["usuario"] = get_current_user().id