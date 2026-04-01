from django.shortcuts import render

def payment(request):
    return render(request,'payment.html')

def register_courses(request):
    return render(request,'register_courses.html')

def view_assignments(request):
    return render(request,'view_assignments.html')

def view_grades(request):
    return render(request,'view_grades.html')
