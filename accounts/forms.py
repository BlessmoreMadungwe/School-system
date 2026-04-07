# accounts/forms.py
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]
    
    role = forms.ChoiceField(choices=ROLE_CHOICES, label="Register as")
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    # --- ADD THIS SECTION BELOW ---
def clean(self):
    cleaned_data = super().clean()
    pw = cleaned_data.get("password")
    cpw = cleaned_data.get("confirm_password")
    if pw and cpw and pw != cpw:
        self.add_error("confirm_password", "Passwords do not match.")
    return cleaned_data