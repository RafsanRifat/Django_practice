from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.

def loginuser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'invalid User name or Password')
        else:
            messages.error(request, 'invalid User name or Password')
    else:
        form = AuthenticationForm()
        return render(request, 'session/login.html', {'form': form})



def logoutuser(request):
    logout(request)
    messages.success(request, "Successfully loged out")
    return redirect('home')


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm
    return render(request, 'session/signup.html', {'form': form})


def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password successfully changed')
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'session/change_pass.html', {'form': form})