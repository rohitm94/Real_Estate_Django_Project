from django.shortcuts import render, redirect
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        print('login submission')
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        messages.error(request, 'Testing error message')
        print('register submission')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    return redirect('index')
