from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .forms import SubjectForm
from .models import Subject
from departments.models import Department
from staff.models import Staff


@staff_member_required
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New subject added to the curriculum!")
            return redirect('subjects_list') # Make sure this URL name exists
    else:
        form = SubjectForm()
    
    return render(request, 'subject_form.html', {'form': form})

# --- SUBJECTS VIEWS ---

def subjects_list(request):
    # Fetch all subjects and their related department info in one go
    subjects = Subject.objects.select_related('department').all()
    return render(request, 'subjects_list.html', {'subjects': subjects})

def subject_detail(request, subject_id):
    # Retrieve the subject or show a 404 error if it doesn't exist
    subject = get_object_or_404(Subject, id=subject_id)
    
    # Optional: Get other subjects from the same department as "Related Courses"
    related_subjects = Subject.objects.filter(
        department=subject.department
    ).exclude(id=subject.id)[:3]

    return render(request, 'subject_detail.html', {
        'subject': subject,
        'related_subjects': related_subjects
    })

def dept_courses(request, dept_id):
    # Fetch the department or 404
    department = get_object_or_404(Department, id=dept_id)
    
    # Filter subjects by that department
    subjects = Subject.objects.filter(department=department)
    
    context = {
        'department': department,
        'subjects': subjects,
    }
    
    # --- MISSING LINE ADDED BELOW ---
    return render(request, 'dept_courses.html', context)
   
def assign_teacher(request, subject_id):
    # 1. Get the subject we want to update
    subject = get_object_or_404(Subject, id=subject_id)
    
    # 2. Get all staff members to populate the dropdown
    staff_members = Staff.objects.all()

    if request.method == "POST":
        teacher_id = request.POST.get('teacher_id')
        if teacher_id:
            # 3. Fetch the selected teacher
            teacher = get_object_or_404(Staff, id=teacher_id)
            # 4. Assign and Save
            subject.teacher = teacher
            subject.save()
            # 5. Redirect back to the department curriculum using the subject's dept ID
            return redirect('dept_courses', dept_id=subject.department.id)

    return render(request, 'assign_teacher.html', {
        'subject': subject,
        'staff_members': staff_members
    })