from django.contrib import admin
from .models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'department', 'credits')
    list_filter = ('department', 'credits')
    search_fields = ('name', 'code')