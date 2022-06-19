from django import forms
from WAD.models import LogMessage
class LogForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("name", "plan")