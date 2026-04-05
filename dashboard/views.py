from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_redirect(request):
    # """ Routes the user to the correct dashboard based on their group """
    if request.user.is_superuser:
        return redirect('admin_dashboard')
    elif hasattr(request.user, 'teacher_profile'):
        return redirect('teacher_dashboard')
    else:
        return redirect('student_dashboard')

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def student_dashboard(request):
    return render(request,'student_dashboard.html')

def teacher_dashboard(request):
    return render(request,'teacher_dashboard.html')

