from django.shortcuts import render

def dept_courses(request):
    return render(request,'dept_courses.html')

def dept_staff(request):
    return render(request,'dept_staff.html')

def departments_list(request):
    return render(request,'departments_list.html')
  
