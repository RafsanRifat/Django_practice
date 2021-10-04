from django.shortcuts import render
from .models import Contact,Post
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
        if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # text = form.cleaned_data['text']
            # obj = Contact(name=name, email=email, text=text)
            # obj.save()    # django form er khetre code gulo dorkar, r Model form use korle code gulo use na kore form.save() diyeai kaj hbe
            form.save()  # uporer code gulo na use kore eita use korleo form data save hobe database a
    else:
        form = ContactForm()
    contex = {'form': form}

    return render(request, 'contact.html', contex)


def post(request):
    post = Post.objects.all()
    return render(request, 'post.html')
