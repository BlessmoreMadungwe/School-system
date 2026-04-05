from django import forms
from .models import Subject

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        # Adjust these fields based on your actual Subject model
        fields = ['name', 'code', 'description', 'department', 'credits']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Advanced Mathematics'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., MATH101'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief course overview...'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'credits': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '10'}),
        }