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
    zip_code = forms.IntegerField(label="Zip Code", required=False)


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
            'bath_count', 'description', 'address', 'city', 'state', 'zip_code', 'pet_friendly', 'pets_allowed',
            'amenities', 'utilities_included_in_rent', 'max_tenant_count', 'current_tenant_count', 'is_active'
        )
        widgets = {
            'description': forms.Textarea
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email', 'date_of_birth', 'physical_address', 'city', 'state', 'zip_code',
            'phone_number', 'bio'
        )
        widgets = {
                'bio': forms.Textarea
        }


class CreateUserForm(forms.ModelForm):
    confirm_password = forms.CharField(label="Confirm password", max_length=20, widget=forms.PasswordInput)

    class Meta:
        model = RegisteredUser
        fields = (
            'first_name', 'last_name', 'date_of_birth', 'physical_address', 'city', 'state', 'zip_code', 'phone_number',
            'bio', 'profile_picture', 'is_student', 'email', 'username', 'password'
        )
        labels = {
            'is_student': 'Are you a student? '
        }
        widgets = {
            'password': forms.PasswordInput
        }


class ForgotPasswordForm(forms.Form):
    email = forms.CharField(label="Email", max_length=20)
