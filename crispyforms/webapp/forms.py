from django import forms
from webapp.models import person
class EmpForm(forms.ModelForm):
    class Meta:
        model=person
        fields='__all__'