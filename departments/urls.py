from django.urls import path
from . import views

urlpatterns = [
    path('dept_staff/<int:dept_id>/', views.dept_staff, name='dept_staff'),
    path('add_department/', views.add_department, name='add_department'),
    path('departments_list/', views.departments_list, name='departments_list'),
    path('dept_courses/', views.dept_courses, name='dept_courses'),
    path('edit_department/edit/<int:pk>/', views.edit_department , name='edit_department'),
    path('delete_department/delete/<int:pk>/', views.delete_department , name='delete_department')
   
]