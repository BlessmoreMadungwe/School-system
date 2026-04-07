from django import forms
from .models import Staff
from django.contrib.auth.models import User

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['user', 'role', 'department', 'is_hod', 'specialization', 'experience_years']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'is_hod': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Pure Mathematics'}),
            'experience_years': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show users who are not already staff members
        assigned_staff = Staff.objects.values_list('user_id', flat=True)
        self.fields['user'].queryset = User.objects.exclude(id__in=assigned_staff)