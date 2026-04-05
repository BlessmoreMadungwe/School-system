from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Department
from .forms import DepartmentForm


@staff_member_required
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Department '{form.cleaned_data['name']}' created!")
            return redirect('departments_list')
    else:
        form = DepartmentForm()

    return render(request, 'add_department.html', {'form': form})


def departments_list(request):
    departments = Department.objects.all()
    return render(request, 'departments_list.html', {'departments': departments})


def dept_courses(request):
    return render(request, 'dept_courses.html')


def dept_staff(request):
    return render(request, 'dept_staff.html')