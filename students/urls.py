from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment, name='payment'),
    path('view_grades/', views.view_grades, name='view_grades'),
    path('view_assignments/', views.view_assignments, name='view_assignments'),
    path('register_courses/', views.register_courses, name='register_courses'),
   
]