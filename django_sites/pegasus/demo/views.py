from django.http import HttpResponseRedirect
from django.shortcuts import render
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

            results = Domicile.objects.all().filter(**filters)

            # TODO: Remove DEBUG statements
            print("[DEBUG] Query: %s\nResult Count: %s\nResults: %s" % (filters, len(results), results))

            context = {
                'form': form,
                'search_results': results,
                'search_count': len(results)
            }
            return render(request, 'demo/index.html', {'results': context})

    else:
        form = SearchForm()

    context = {
        'form': form,
        'search_results': []
    }
    return render(request, 'demo/index.html', {'results': context})


def forms_test(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        compatibility_form = CompatibilityScoreForm(request.POST)

    else:
        login_form = LoginForm()
        compatibility_form = CompatibilityScoreForm()

    context = {
        'login': login_form,
        'compatibility': compatibility_form
    }

    return render(request, 'demo/form_test.html', {'context': context})