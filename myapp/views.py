from django.shortcuts import render

# Create your views here.


def home(request):
    name = ['Rifat', 'Tahsin', 'Asif', 'Arman']
    contex = {
        'name':name
    }
    return render(request, 'index.html', contex)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        print(name)
        print(email)
        print(text)
    return render(request, 'contact.html')
