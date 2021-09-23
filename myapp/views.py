from django.shortcuts import render

# Create your views here.


def home(request):
    name = ['Rifat', 'Tahsin', 'Asif', 'Arman']
    contex = {
        'name':name
    }
    return render(request, 'index.html', contex)


def contact(request):
    return render(request, 'contact.html')
