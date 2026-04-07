# admin.py
from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'department', 'is_hod')
    list_filter = ('role', 'department')