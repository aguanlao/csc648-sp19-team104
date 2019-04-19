from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Administrative paths
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # User management paths
    path('create_account/', views.create_account, name='create_account'),
    path('modify_profile/', views.modify_profile, name='modify_profile'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('view_profile/<str:username>/', views.view_profile, name='view_profile'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('compatibility/', views.compatibility_score, name='compatibility'),
    path('forgot/', views.forgot_password, name='forgot_password')
]
