from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'loan_date': forms.DateInput(attrs={'type': 'date'}),
        }
