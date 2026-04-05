from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data
