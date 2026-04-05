
from django.db import models
from django.contrib.auth.models import User
from departments.models import Department 
from subjects.models import Subject       


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    student_id = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='student_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.student_id})"

