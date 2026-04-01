# Subjects
from django.urls import path
from . import views

urlpatterns =[   
    
    path('subjects/', views.subjects_list, name='subjects_list'),
    path('subjects/detail/', views.subject_detail, name='subject_detail'),
]
 