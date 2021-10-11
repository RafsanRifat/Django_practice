from django.shortcuts import render, HttpResponse
from .models import Contact, Post
from .forms import ContactForm, PostForm
from django.views.generic import ListView,DetailView,UpdateView


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




class PostListView(ListView):  # List view
    template_name = 'postlist.html'
    model = Post
    context_object_name = 'postlist'


class PostDetailView(DetailView):
    model = Post
    template_name = 'postdetail.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'postcreate.html'


def post(request):
    post = Post.objects.all()
    contex = {'post': post}
    return render(request, 'post.html', contex)


def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            sub = form.cleaned_data['subject']
            for i in sub:
                obj.subject.add(i)
                obj.save()
            class_in = form.cleaned_data['class_in']
            for i in class_in:
                obj.class_in.add(i)
                obj.save()
            return HttpResponse('Your form is successfully submited')
    else:
        form = PostForm
    contex = {'form': form}
    return render(request, 'postcreate.html', contex)
