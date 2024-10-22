from django.urls import path
from .views import login, success

urlpatterns = [
    path('login', login, name='login'),
    path('success/', success, name='success'),
]