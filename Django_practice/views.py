from django.http import HttpResponse
from django.shortcuts import render

def rafsan(request):
    return render(request, 'index.html')
