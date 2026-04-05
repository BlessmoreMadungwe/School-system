from django.db import models
from django.contrib.auth.models import User
from departments.models import Department
from subjects.models import Subject

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='teachers')
    specialization = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    qualification = models.CharField(max_length=100, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='teacher_pics/', blank=True, null=True)

    def __str__(self):
        return f"Teacher: {self.user.get_full_name()} ({self.employee_id})"

class StudyMaterial(models.Model):
    title = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    file = models.FileField(upload_to='study_materials/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title