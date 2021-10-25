from django.urls import path, include
from .views import loginuser, logoutuser, registration, changepassword

urlpatterns = [
    path('login/', loginuser, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('signup/', registration, name='signup'),
    path('changepassword/', changepassword, name='changepassword'),
]
