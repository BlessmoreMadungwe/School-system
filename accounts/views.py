from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# --- REMOVE UserCreationForm FROM THE LINE BELOW ---
from .forms import RegisterForm 
from students.models import Student
from teachers.models import Teacher


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # 1. Save the basic User account
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            
            role = form.cleaned_data.get('role')
            
            # 2. If Admin, give them staff status so they can log into /admin/
            if role == 'admin':
                user.is_staff = True
                user.is_superuser = True # Optional: Full control
            
            user.save()

            # 3. Create the profile so they appear in the Admin tables
            if role == 'student':
                Student.objects.create(user=user, student_id=f"STU-{user.id}")
                
            elif role == 'teacher':
                # This makes them show up in the "Teachers" section of your screenshot
                Teacher.objects.create(user=user, employee_id=f"TCH-{user.id}")

            # 4. Log them in and go home
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')