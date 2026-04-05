from django.db import models
from departments.models import Department

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    
    # Changed from CharField(10) to TextField for actual course descriptions
    description = models.TextField(blank=True, null=True)
    
    # Linked to Department (Good job on the ForeignKey!)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subjects')
    
    credits = models.PositiveIntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code}: {self.name}"

    class Meta:
        ordering = ['code'] # Keeps your list alphabetical by code