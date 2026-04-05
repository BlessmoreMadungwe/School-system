from django.db import models
from django.contrib.auth.models import User
from teachers.models import Teacher
from departments.models import Department
from subjects.models import Subject

class ClassAssignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classes')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.teacher.user.last_name} - {self.subject.name}"
    

