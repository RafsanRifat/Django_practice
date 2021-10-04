from .views import home,contact,post
from django.urls import path,include

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('post/', post, name='post')
]