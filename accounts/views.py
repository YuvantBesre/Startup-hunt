from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def SignUpPage(request):

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                ExistingUser = User.objects.get(username = request.POST['username'])
                return render(request, 'accounts/register.html', {'error' : 'User already exist, please try again!'})
            except User.DoesNotExist:
                NewUser = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                auth.login(request, NewUser)
                return redirect('home')
        else:
            return render(request, 'accounts/register.html', {'error' : 'Password must match'})
    else:
        return render(request, 'accounts/register.html')


def LoginPage(request):

    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error' : 'Username or Password is incorrect, please try again'})
    else:
        return render(request, 'accounts/login.html')


def Logout(request):

    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

