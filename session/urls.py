from django.urls import path, include
from .views import loginuser

urlpatterns = [
    path('login/', loginuser, name='login' )
]
