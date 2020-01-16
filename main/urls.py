"""Main app urls."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.static_tests_list, name='static_test_lists'),
]
