# from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from main.forms import CreateUserForm


def index(request):

    context = {
        'values': ['Test 1', 'Test 2']
    }

    return render(request, 'main/index.html', context)


def loginPage(request):
    return render(request, 'main/login.html')


def registerPage(request):
    form = CreateUserForm()

    context = {
        'form':form
    }
    return render(request, 'main/register.html')
