from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #TEST
    path('test/', views.test, name='test'),
    #admin
    path('admin/', views.admin, name='admin'),
    #index
    path('home/', views.user_login, name='homepage'),
    #sign up
    path('signup/', views.signup, name='signup'), #the new page
    #add_new_property
    path('add_new_property/', views.create_listing, name='add_new_property'),
    #listing
    path('listing/', views.index, name='listing'), 
    #description
    path('description/', views.description, name='description'),
    #manager_profile
    path('manager_profile/', views.manager_profile, name='manager_profile'),
    #survey
    path('survey/', views.survey, name='survey'),
    #user_profile
    path('user_profile/', views.user_profile, name='user_profile'),
    # Administrative paths
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    re_path(
        r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'
    ),

    # User management paths
    path('create_account/', views.create_account, name='create_account'),
    path('modify_profile/', views.modify_profile, name='modify_profile'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('view_profile/<str:username>/', views.view_profile, name='view_profile'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('compatibility/', views.compatibility_score, name='compatibility'),

    # Listing paths
    path('create_listing/', views.create_listing, name='create_listing'),
    path('<int:listing_id>/', views.view_listing, name='view_listing'),
    path('<int:listing_id>/edit/', views.edit_listing, name='edit_listing'),

    # SNN paths
    path('create_group/', views.create_group, name='create_group'),
    path('edit_group/<str:group_name>/', views.edit_group, name='edit_group'),
    path('delete_group/<str:group_name>/', views.delete_group, name='delete_group'),
    path('view_group/<str:group_name>/', views.view_group, name='view_group'),
]
