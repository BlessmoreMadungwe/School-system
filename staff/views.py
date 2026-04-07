from django.shortcuts import render, redirect
from .forms import StaffForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Staff

def add_staff(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Staff member added successfully!")
            return redirect('departments_list') # Or wherever your staff list is
    else:
        form = StaffForm()
    
    return render(request, 'add_staff.html', {'form': form})


def staff_profile(request, staff_id):
    # Fetch the staff member using the ID from the URL
    staff = get_object_or_404(Staff, id=staff_id)
    
    context = {
        'staff': staff,
    }
    return render(request, 'staff_profile.html', context)