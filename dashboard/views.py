
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'dashboard/login.html', {'form': {'errors': True}})
    return render(request, 'dashboard/login.html')

def user_logout(request):
    logout(request)
    return redirect('/login')

@login_required
def dashboard(request):
    return render(request, 'dashboard/home.html')
