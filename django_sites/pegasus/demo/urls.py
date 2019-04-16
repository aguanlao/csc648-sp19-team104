from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form_test/', views.forms_test, name='forms_test'),
]