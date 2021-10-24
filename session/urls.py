from django.urls import path, include
from .views import loginuser, logoutuser, registration

urlpatterns = [
    path('login/', loginuser, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('signup/', registration, name='signup'),
]
