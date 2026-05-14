# Subjects
from django.urls import path
from . import views

urlpatterns =[   
    
    path('subjects/', views.subjects_list, name='subjects_list'),
    path('subjects_detail/<int:subject_id>/', views.subject_detail, name='subject_detail'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('dept_courses/<int:dept_id>/', views.dept_courses, name='dept_courses'),
    path('assign_teacher/<int:subject_id>/', views.assign_teacher, name='assign_teacher'),
   
]
