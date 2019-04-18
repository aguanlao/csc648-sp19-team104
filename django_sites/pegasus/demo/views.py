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
                if value is not '' and
                   value is not False and
                   value is not None and
                   '%s'.lower() % value != 'all'
            }

            # results = Domicile.objects.all().filter(**filters)

            # TODO: Remove DEBUG statements
            # print("[DEBUG] Query: %s\nResult Count: %s\nResults: %s" % (filters, len(results), results))
            print("[DEBUG] Received form data!")
            for key, value in filters.items():
                print("[DEBUG] (%s , %s)" % (key, value))

            context = {
                'form': form,
                # 'search_results': results,
                # 'search_count': len(results)
            }
            return render(request, 'demo/search.html', {'results': context})

    else:
        form = SearchForm()

    context = {
        'form': form,
        'search_results': []
    }
    return render(request, 'demo/search.html', {'results': context})


# USER PAGES #
def compatibility_score(request):
    if request.method == 'POST':
        compatibility_form = CompatibilityScoreForm(request.POST)
        if compatibility_form.is_valid():
            # TODO: Remove debug statements
            print("[DEBUG] Received compatibility form data!")
            for key, value in compatibility_form.cleaned_data.items():
                print("[DEBUG] (%s , %s)" % (key, value))
    else:
        compatibility_form = CompatibilityScoreForm()

    context = {
        'compatibility_form': compatibility_form
    }

    return render(request, 'demo/compatibility_score.html', {'context': context})


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            form_data = {
                key: value for key, value in login_form.cleaned_data.items()
            }

            username = form_data['username']
            password = form_data['password']
            auth_backend = utils.AuthBackend()
            user = auth_backend.authenticate(username=username, password=password)

            # Login success
            if user is not None:
                login(request, user)

                pprint(request.POST)

                # Check if user needs to redirect to another page other than index
                next_url = request.POST.get('next', '')
                if next_url:
                    return redirect(next_url)
                else:
                    return HttpResponseRedirect(reverse('index'))

            # Login failure
            else:
                context = {
                    'login_form': login_form,
                    'error_message': 'Username or password is incorrect.'
                }

        else:
            context = {
                'login_form': login_form,
                'error_message': '%s' % login_form.errors
            }

    else:
        login_form = LoginForm()
        context = {
            'login_form': login_form,
            'error_message': ''
        }
    return render(request, 'demo/login.html', {'context': context})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse("You are logged in '%s'." % request.user.username)


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

    return render(request, 'demo/create_account.html', {'results': context})


def delete_user(request):
    if request.method == 'POST':
        delete_user_form = DeleteUserForm(request.POST)
        if delete_user_form.is_valid():
            # TODO: Remove debug statements
            print("[DEBUG] Received delete user form data!")
            print("[DEBUG] Comment: %s" % delete_user_form.cleaned_data['comment'])
    else:
        delete_user_form = DeleteUserForm()

    context = {
        'delete_user_form': delete_user_form
    }

    return render(request, 'demo/delete_account.html', {'context': context})


def edit_user(request):
    if request.method == 'POST':
        edit_user_form = EditUserForm(request.POST)
        if edit_user_form.is_valid():
            filtered_data = remove_empty_dict(**edit_user_form.cleaned_data)

            # TODO: Remove debug statements
            print("[DEBUG] Received edit user form data!")
            for key, value in filtered_data.items():
                print("[DEBUG] (%s , %s)" % (key, value))
                
    else:
        edit_user_form = EditUserForm()

    context = {
        'edit_user_form': edit_user_form
    }

    return render(request, 'demo/modify_profile.html', {'context': context})


def remove_empty_dict(**input_dict):
    filtered_dict = {
        key: value for key, value in input_dict.items()
        if value is not '' and
           value is not False and
           value is not None
    }

    return filtered_dict
