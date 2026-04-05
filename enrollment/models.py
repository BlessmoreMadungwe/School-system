from django.db import models
from django.contrib.auth.models import User
from subjects.models import Subject 
from students.models import Student


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10)
    enrollment_date = models.DateField(auto_now_add=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    @property
    def grade(self):
        if self.score is None: return "N/A"
        if self.score >= 90: return 'A'
        if self.score >= 80: return 'B'
        if self.score >= 70: return 'C'
        if self.score >= 60: return 'D'
        return 'F'

    def __str__(self):
        return f"{self.student.user.username} - {self.subject.name}"