from django import forms
from .models import *

class SearchForm(forms.Form):
    form_residence_options = [('all', 'All')] + Domicile.residence_options
    residence_type = forms.ChoiceField(label="Residence type", choices=form_residence_options, required=False)
    pet_friendly = forms.BooleanField(label="Allows pets", required=False)
    city = forms.CharField(label="City", max_length=20, required=False)