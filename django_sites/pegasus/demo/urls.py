from django.urls import path, include
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

    #Listing paths
    path('create_listing/', views.create_listing, name='create_listing'),
    path('<int:listing_id>/', views.view_listing, name='view_listing'),
    path('<int:listing_id>/edit/', views.edit_listing, name='edit_listing'),
]
