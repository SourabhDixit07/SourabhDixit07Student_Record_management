from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, StudentForm
from .models import Student

# Register view (corrected)
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Optionally log the user in after registration
            return redirect('dashboard')
        else:
            print(form.errors)  # Debugging help
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard on successful login
    return render(request, 'login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard view (requires login)
@login_required
def dashboard(request):
    students = Student.objects.all()
    return render(request, 'dashboard.html', {'students': students})

# Add student
@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

# Edit student
@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})

# Delete student
@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('dashboard')

# Profile page
@login_required
def profile(request):
    return render(request, 'profile.html')

# About page
def about(request):
    return render(request, 'about.html')
