# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from main.forms import CreateUserForm


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    is_teacher = request.user.groups.filter(name='teachers').exists()

    context = {
        'values': ['Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2',
                   'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2', 'Test 1', 'Test 2'],
        'username': request.user.username,
        'role': 'teacher' if is_teacher else 'student',

    }

    return render(request, 'main/index.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Username OR password is incorrect')

    return render(request, 'main/login.html')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserForm()
    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'main/register.html', context)


def teacherCabinet(request):
    context = {
        'schedule': 'Edit Schedule',
        'grades': 'Edit Grades'
    }
    return render(request, 'main/teacher-cabinet.html', context)


def studentCabinet(request):
    context = {
        'schedule': 'View Schedule',
        'grades': 'View Grades'
    }
    return render(request, 'main/student-cabinet.html', context)