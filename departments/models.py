from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True) # e.g., 'CS', 'MATH'
    description = models.TextField(blank=True, null=True)
    established_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"