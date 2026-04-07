from django.urls import path
from . import views

urlpatterns = [
    # Path to add a new staff member
    path('add_staff/', views.add_staff, name='add_staff'),
    
    # # Path to view a specific staff profile
    path('profile/<int:staff_id>/', views.staff_profile, name='staff_profile'),
]