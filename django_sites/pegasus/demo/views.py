from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import utils
from .forms import *
from .models import *
from pprint import pprint


# LISTING PAGES #
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():

            # Filter all null values from filter set
            filters = {
                key: value for key, value in form.cleaned_data.items()
                if value is not '' and value is not False and value is not None and '%s'.lower() % value != 'all'
            }

            # results = Domicile.objects.all().filter(**filters)

            # TODO: Remove DEBUG statements
            results = []
            for key, value in filters.items():
                print("[DEBUG] (%s , %s)" % (key, value))

            context = {
                'form': form,
                'search_results': results,
                'search_count': len(results)
            }
            return render(request, 'demo/search.html', {'context': context})

    else:
        form = SearchForm()

    context = {
        'form': form,
        'search_results': []
    }
    return render(request, 'demo/search.html', {'context': context})


# USER PAGES #
def create_account(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user_attributes = {
                key: value for key, value in form.cleaned_data.items()
            }

            # Encrypt password before creating account
            user_attributes.pop('confirm_password')
            secret = '%s' % user_attributes.get('password', '')
            secret = utils.encrypt_password(secret)
            user_attributes['password'] = secret

            try:
                user = RegisteredUser()
                user.update(**user_attributes)
                user.save()

                context = {
                    'form': form,
                    'creation_success': True,
                    'form_submitted': True,
                    'error_message': ''
                }

            except Exception as error_message:
                context = {
                    'form': form,
                    'creation_success': False,
                    'form_submitted': True,
                    'error_message': '%s' % error_message
                }

        else:
            context = {
                'form': form,
                'creation_success': False,
                'form_submitted': False,
                'error_message': '%s.' % form.errors
            }

    else:
        form = CreateUserForm()
        context = {
            'form': form,
            'creation_success': False,
            'form_submitted': False,
            'error_message': ''
        }

    return render(request, 'demo/create_account.html', {'context': context})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form_data = {
                key: value for key, value in form.cleaned_data.items()
            }

            username = form_data['username']
            password = form_data['password']
            auth_backend = utils.AuthBackend()
            user = auth_backend.authenticate(username=username, password=password)

            # Login success
            if user is not None:
                login(request, user, backend='demo.utils.AuthBackend')

                # Check if user needs to redirect to another page other than index
                next_url = request.POST.get('next', '')
                if next_url:
                    return redirect(next_url)
                else:
                    return HttpResponseRedirect(reverse('index'))

            # Login failure
            else:
                context = {
                    'login_form': form,
                    'error_message': 'Username or password is incorrect.'
                }

        else:
            context = {
                'login_form': form,
                'error_message': '%s' % form.errors
            }

    else:
        form = LoginForm()
        context = {
            'login_form': form,
            'error_message': ''
        }
    return render(request, 'demo/login.html', {'context': context})


@login_required
def compatibility_score(request):
    if request.method == 'POST':
        compatibility_form = CompatibilityScoreForm(request.POST)
        if compatibility_form.is_valid():
            pass

    else:
        compatibility_form = CompatibilityScoreForm()

    context = {
        'form': compatibility_form
    }

    return render(request, 'demo/compatibility_score.html', {'context': context})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def view_profile(request, username=None):
    try:

        # If no username is provided, default to currently logged in account
        if username is None:
            username = request.user.username

        user_instance = RegisteredUser.objects.get(username=username)
        if user_instance:
            context = {
                'user_found': True,
                'user': user_instance,
                'error_message': ''
            }
        else:
            context = {
                'user_found': False,
                'user': None,
                'error_message': "User '%s' not found." % username
            }

    except Exception as error_message:
        context = {
            'user_found': False,
            'user': None,
            'error_message': "User '%s' not found." % username
        }

    return render(request, 'demo/view_profile.html', {'context': context})


@login_required
def modify_profile(request):
    current_user = request.user.username
    user_instance = RegisteredUser.objects.get(username=current_user)

    if request.method == 'POST':
        form = EditUserForm(request.POST)
        if form.is_valid():
            user_attributes = {
                key: value for key, value in form.cleaned_data.items()
            }

            try:
                user_instance.update(**user_attributes)
                user_instance.save()

                context = {
                    'form': form,
                    'update_success': True,
                    'error_message': ''
                }

            except Exception as error_message:
                context = {
                    'form': form,
                    'update_success': False,
                    'error_message': '%s' % error_message
                }

        else:
            context = {
                'form': form,
                'update_success': False,
                'error_message': '%s.' % form.errors
            }

    else:
        form = EditUserForm(instance=user_instance)
        context = {
            'form': form,
            'update_success': False,
            'error_message': ''
        }
    return render(request, 'demo/modify_profile.html', {'context': context})


@login_required
def delete_user(request):
    if request.method == 'POST':
        form = DeleteUserForm(request.POST)
        if form.is_valid():
            pass

    else:
        form = DeleteUserForm()

    context = {
        'form': form
    }

    return render(request, 'demo/delete_account.html', {'context': context})


@login_required
def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            pass

    else:
        form = ForgotPasswordForm()

    context = {
        'form': form
    }

    return render(request, 'demo/forgot_password.html', {'context': context})
