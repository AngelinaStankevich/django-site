from django.urls import path

from .views import *

urlpatterns = [

    path('', index),  # http://127.0.0.1:8000/furniture/
    path('cats/', categories),  # http://127.0.0.1:8000/furniture/cats/
]
