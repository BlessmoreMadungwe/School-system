from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .forms import SubjectForm
from .models import Subject

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

def subject_detail(request):
    return render(request, 'subject_detail.html')
