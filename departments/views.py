from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Department 
from staff.models import Staff
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

def dept_staff(request, dept_id):
   # Fetch the department or return 404 if not found
    department = get_object_or_404(Department, id=dept_id)
    
    # Fetch all staff members assigned to this department
    # This assumes your Staff model has a foreign key to Department
    staff_members = Staff.objects.filter(department=department)
    
    context = {
        'department': department,
        'staff_members': staff_members,
        'staff_count': staff_members.count()
    }
    return render(request, 'dept_staff.html', context )
# EDIT VIEW
def edit_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('departments_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'edit_department.html', {'form': form, 'department': department})

# DELETE VIEW
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        department.delete()
        return redirect('departments_list')
    
    return render(request, 'delete_department.html', {'department': department})