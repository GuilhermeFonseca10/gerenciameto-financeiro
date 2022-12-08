from django import forms
from crum import get_current_user
from .models import Lancamento
from .models import Conta


class LancamentoForm(forms.ModelForm):
    class Meta:
        model = Lancamento
       

        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LancamentoForm, self).__init__(*args, **kwargs)
        self.initial["usuario"] = get_current_user().id
    