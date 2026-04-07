from django.db import models
from django.contrib.auth.models import User
from departments.models import Department

class Staff(models.Model):
    ROLE_CHOICES = [
        ('HEADMASTER', 'Headmaster'),
        ('DEPUTY_HEAD', 'Deputy Headmaster'),
        ('SENIOR_TEACHER', 'Senior Teacher'),
        ('TEACHER', 'Teacher'),
        ('COACH', 'Sports Coach'),
        ('ADMIN', 'Administrator'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_hod = models.BooleanField(default=False, verbose_name="Head of Department")
    department = models.ForeignKey('departments.Department', on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='TEACHER')
    experience_years = models.PositiveIntegerField(default=0)
    specialization = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.get_role_display()})"