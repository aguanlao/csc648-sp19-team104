from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Administrative paths
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('special/', views.special, name='special'),
    path('logout/', views.user_logout, name='logout'),

    # User management paths
    path('create_account/', views.create_account, name='create_account'),
    path('edit_user/', views.edit_user, name='edit_user'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('compatibility/', views.compatibility_score, name='compatibility'),
]