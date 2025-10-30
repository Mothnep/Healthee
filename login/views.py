from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate  
from django.contrib import messages  
from django.contrib.auth.models import User

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if that username exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('login')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('login')
        else:
            auth_login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('profile')

    return render(request, 'login.html')