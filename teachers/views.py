from django.shortcuts import render

def my_classes(request):
    return render(request, 'my_classes.html')

def enter_grades(request):
    return render(request, 'enter_grades.html')

def upload_material(request):
    return render(request, 'upload_material.html')

def attendance(request):
    # Just a placeholder for now
    return render(request, 'attendance.html')