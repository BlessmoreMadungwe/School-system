from django.urls import path
from . import views

# Setting app_name makes it easier to reference (e.g., 'teachers:my_classes')
app_name = 'teachers'

urlpatterns = [
    path('my-classes/', views.my_classes, name='my_classes'),
    path('enter-grades/', views.enter_grades, name='enter_grades'),
    path('upload-material/', views.upload_material, name='upload_material'),
    path('attendance/', views.attendance, name='attendance'),
]