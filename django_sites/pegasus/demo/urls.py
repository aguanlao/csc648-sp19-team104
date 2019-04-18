from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compatibility/', views.compatibility_score, name='compatibility'),
    # path('login/', views.login, name='login'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('edit_user/', views.edit_user, name='edit_user'),
    path('create_account/', views.create_account, name='create_account')
]