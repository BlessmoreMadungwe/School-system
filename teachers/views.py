from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MaterialUploadForm

def my_classes(request):
    return render(request, 'my_classes.html')

def enter_grades(request):
    return render(request, 'enter_grades.html')

def upload_material(request):
    if request.method == 'POST':
        # request.FILES is required for file uploads!
        form = MaterialUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Study material uploaded successfully!")
            return redirect('teacher_dashboard') # Or wherever you want them to go
    else:
        form = MaterialUploadForm()
    
    return render(request, 'upload_material.html', {'form': form})

def attendance(request):
    # Just a placeholder for now
    return render(request, 'attendance.html')