from WebAsha.models import booking
from django import forms

class bookingForm(forms.ModelForm):
    class Meta:
        model=booking
        fields='__all__'