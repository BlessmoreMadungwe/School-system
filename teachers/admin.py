# teachers/admin.py
from django.contrib import admin
from .models import Teacher,StudyMaterial

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # This pulls the name from the linked User account
    list_display = ('employee_id', 'get_name', 'department')

    def get_name(self, obj):
        return obj.user.get_full_name() or obj.user.username
    get_name.short_description = 'Name'

admin.site.register(StudyMaterial)