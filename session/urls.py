from django.urls import path, include
from .views import loginuser, logoutuser, registration, changepassword
from django.contrib.auth.views import PasswordResetView, PasswordChangeDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('login/', loginuser, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('signup/', registration, name='signup'),
    path('changepassword/', changepassword, name='changepassword'),
]
