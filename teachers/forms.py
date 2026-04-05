from django import forms
from .models import StudyMaterial

class MaterialUploadForm(forms.ModelForm):
    class Meta:
        model = StudyMaterial
        fields = ['subject', 'title', 'file']
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Chapter 1 Notes'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }