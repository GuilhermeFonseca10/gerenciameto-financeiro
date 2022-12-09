from django import forms
from crum import get_current_user
from .models import Lucro
from .models import Conta


class LucroForm(forms.ModelForm):
    class Meta:
        model = Lucro
       

        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LucroForm, self).__init__(*args, **kwargs)
        self.initial["usuario"] = get_current_user().id
    