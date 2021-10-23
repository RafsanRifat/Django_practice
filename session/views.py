from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

def loginuser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid()():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
    return render(request, 'session/login.html')
