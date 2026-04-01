from django.urls import path
from . import views

urlpatterns = [
    path('departments_list/', views.departments_list, name='departments_list'),
    path('dept_courses/', views.dept_courses, name='dept_courses'),
    path('dept_staff/', views.dept_staff, name='dept_staff'),
   
   
]