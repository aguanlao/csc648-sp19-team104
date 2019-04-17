from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import SearchForm, LoginForm, CompatibilityScoreForm
from .models import *
# import logging
# from pprint import pprint

# # Get instance of default logger
# logger = logging.getLogger(__name__)


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


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # TODO: Remove debug statements
            print("[DEBUG] Received login form data!")
            for key, value in login_form.cleaned_data.items():
                print("[DEBUG] (%s , %s)" % (key, value))

            return redirect(index)
    else:
        login_form = LoginForm()

    context = {
        'login_form': login_form,
    }

    return render(request, 'demo/login.html', {'context': context})
