from django.shortcuts import render
from .models import Contact
from .forms import ContactForm


# Create your views here.


def home(request):
    name = ['Rifat', 'Tahsin', 'Asif', 'Arman']
    contex = {
        'name': name
    }
    return render(request, 'index.html', contex)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        obj = Contact(name=name, email=email, text=text)
        obj.save()
    else:
        form = ContactForm()

    contex = {'form': form}

    return render(request, 'contact.html', contex)
