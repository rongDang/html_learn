from bs4.views import *
from django.urls import path

urlpatterns = [
    path('', login, name='login'),
]
