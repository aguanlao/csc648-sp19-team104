from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compatibility/', views.compatibility_score, name='compatibility'),
    path('login/', views.login, name='login'),
]