from django import forms
from .models import *

class SearchForm(forms.Form):
    form_residence_options = [('all', 'All')] + Domicile.residence_options
    residence_type = forms.ChoiceField(label="Residence type", choices=form_residence_options, required=False)
    pet_friendly = forms.BooleanField(label="Allows pets", required=False)
    city = forms.CharField(label="City", max_length=20, required=False)


class LoginForm(forms.Form):
    MAX_FIELD_LENGTH = 20
    username = forms.CharField(label="Username", max_length=MAX_FIELD_LENGTH)
    password = forms.CharField(label="Password", max_length=MAX_FIELD_LENGTH, widget=forms.PasswordInput)


class CompatibilityScoreForm(forms.Form):
    SCALE_CHOICES = [
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')
    ]
    cleanliness = forms.ChoiceField(label="Cleanliness", choices=SCALE_CHOICES, widget=forms.RadioSelect)
    socialness = forms.ChoiceField(label="Socialness", choices=SCALE_CHOICES, widget=forms.RadioSelect)
    partyness = forms.ChoiceField(label="Partyness", choices=SCALE_CHOICES, widget=forms.RadioSelect)