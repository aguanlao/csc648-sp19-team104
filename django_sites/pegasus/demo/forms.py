from django import forms
from .models import *

class SearchForm(forms.Form):
    form_residence_options = [('all', 'All')] + Domicile.residence_options
    residence_type = forms.ChoiceField(label="Residence type", choices=form_residence_options, required=False)
    pet_friendly = forms.BooleanField(label="Allows pets", required=False)
    beds = forms.IntegerField(label="Beds", min_value=0, required=False)
    baths = forms.IntegerField(label="Baths", min_value=0, required=False)
    size_sq_ft = forms.FloatField(label="Square Footage", min_value=0.0, required=False)
    price = forms.FloatField(label="Price", min_value=0.0, required=False)
    city = forms.CharField(label="City", max_length=20, required=False)
    #ZIP Codes limited to within CA
    zip = forms.IntegerField(label="Zip Code", min_value=90001, max_value=96162, required=False)


class LoginForm(forms.Form):
    MAX_FIELD_LENGTH = 20
    username = forms.CharField(label="Username", max_length=MAX_FIELD_LENGTH)
    password = forms.CharField(label="Password", max_length=MAX_FIELD_LENGTH, widget=forms.PasswordInput)


class CompatibilityScoreForm(forms.Form):
    SCALE_CHOICES = [
        (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
    ]
    # TODO: Define all attributes/fields for compatibility score
    cleanliness = forms.ChoiceField(label="Cleanliness", choices=SCALE_CHOICES, widget=forms.RadioSelect)
    socialness = forms.ChoiceField(label="Socialness", choices=SCALE_CHOICES, widget=forms.RadioSelect)
    partyness = forms.ChoiceField(label="Partyness", choices=SCALE_CHOICES, widget=forms.RadioSelect)


class DeleteUserForm(forms.Form):
    comment = forms.CharField(label="Comments", max_length=250, widget=forms.Textarea)


class EditListingForm(forms.ModelForm):
    class Meta:
        # TODO: Uncomment ValidListing model once models are complete
        # model = ValidListing
        fields = (
            'title', 'residence_type', 'price', 'agent', 'available', 'size_sq_ft', 'bed_count',
            'bath_count', 'description', 'address', 'city', 'state', 'zip'
        )
        widgets = {
            'description': forms.Textarea
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email', 'date_of_birth', 'physical_address', 'city', 'state', 'zip',
            'phone_number', 'description'
        )
        widgets = {
            'description': forms.Textarea
        }


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'password', 'date_of_birth',
            'physical_address', 'email', 'is_student'
        )
        widgets = {
            'password': forms.PasswordInput
        }
