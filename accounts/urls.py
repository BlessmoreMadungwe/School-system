from django.urls import path
from .views import register_view, login_view, logout_view

urlpatterns = [
    path('login_view/', login_view, name='login_view'),
    path('logout_view/', logout_view, name='logout_view'),
    path('register_view/', register_view, name='register_view'),
    
]