from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserCreationForm ,RegisterForm

# ✅ REGISTER VIEW
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST) # Use your RegisterForm, not UserCreationForm
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            # This helps you see why registration failed (e.g. weak password)
            print(form.errors)
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()

    # CRITICAL: You must pass {'form': form} so the HTML can see the fields
    return render(request, 'register.html', {'form': form}) 

# ✅ LOGIN VIEW (CUSTOM)
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


# ✅ LOGOUT VIEW (OPTIONAL CUSTOM)
def logout_view(request):
    logout(request)
    return redirect('home')