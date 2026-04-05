
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('core.urls')),
    path('', include('dashboard.urls')),
    path('', include('students.urls')),
    path('', include('teachers.urls')),
    path('', include('departments.urls')),
    path('', include('subjects.urls')),
    path('', include('assignment.urls')),
    path('', include('enrollment.urls')),
  
]
