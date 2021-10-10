from .views import home,contact,post,postcreate,PostListView
from django.urls import path,include

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('post/', post, name='post'),
    path('postcreate/', postcreate, name='postcreate'),
    path('postlist/', PostListView, name='postlistview'),
]