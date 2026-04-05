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
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # This adds the Bootstrap class to EVERY input automatically
            field.widget.attrs['class'] = 'form-control'
    # ------------------------------