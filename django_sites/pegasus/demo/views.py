from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SearchForm
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