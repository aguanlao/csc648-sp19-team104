from django.forms import formset_factory
from django.forms.formsets import BaseFormSet
from django import forms
from .models import *


class SearchForm(forms.Form):
    form_residence_options = [('all', 'All')] + Domicile.residence_options
    residence_type = forms.ChoiceField(label="Residence type", choices=form_residence_options, required=False)
    pet_friendly = forms.BooleanField(label="Allows pets", required=False)
    utilities_included_rent = forms.BooleanField(label="Utilities Included", required=False)
    bed_count = forms.IntegerField(label="Bedrooms", min_value=0, required=False)
    bath_count = forms.IntegerField(label="Bathrooms", min_value=0, required=False)
    size = forms.FloatField(label="Square Footage", min_value=0.0, required=False)
    min_price = forms.FloatField(label="Min Price", min_value=0.0, required=False)
    max_price = forms.FloatField(label="Max Price", min_value=0.0, required=False)
    city = forms.CharField(label="City", max_length=20, required=False)
    zip_code = forms.IntegerField(label="Zip Code", required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['city'].widget.attrs['placeholder'] = 'Search By City'
        self.fields['bed_count'].widget.attrs['placeholder'] = '# Bed'
        self.fields['bath_count'].widget.attrs['placeholder'] = '# Bath'


class LoginForm(forms.Form):
    MAX_FIELD_LENGTH = 20
    username = forms.CharField(label="username", max_length=MAX_FIELD_LENGTH, widget=forms.TextInput(
        attrs={
            'class': 'form-control col-auto',
            'placeholder': 'username'
        }
    ))
    password = forms.CharField(
        label="password", help_text='max 20 characters', max_length=MAX_FIELD_LENGTH, widget=forms.PasswordInput(
            attrs={
                'class': 'form-control col-auto',
                'placeholder': 'password'
            }
        ))


class CompatibilityScoreForm(forms.Form):
    SCALE_CHOICES = [
        (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
    ]
    cleanliness = forms.ChoiceField(label="Cleanliness", choices=SCALE_CHOICES, widget=forms.RadioSelect)
    socialness = forms.ChoiceField(label="Socialness", choices=SCALE_CHOICES, widget=forms.RadioSelect)
    partyness = forms.ChoiceField(label="Partyness", choices=SCALE_CHOICES, widget=forms.RadioSelect)


class DeleteUserForm(forms.Form):
    comment = forms.CharField(label="Comments", max_length=250, widget=forms.Textarea)


class CreateDomicileForm(forms.ModelForm):
    class Meta:
        model = Domicile
        fields = (
            'residence_type', 'address', 'city', 'state', 'zip_code', 'size', 'bed_count', 'bath_count',
            'price', 'pet_friendly', 'pets_allowed', 'limit_tenant_count', 'current_tenant_count', 'amenities',
            'utilities_included_rent', 'is_active', 'description', 'photo', 'district'
        )
        widgets = {
            'pets_allowed': forms.Textarea,
            'description': forms.Textarea,
        }


class EditListingForm(forms.ModelForm):
    class Meta:
        model = Domicile
        fields = (
            'owner', 'price',  'pet_friendly', 'pets_allowed', 'limit_tenant_count', 'current_tenant_count', 'amenities',
            'utilities_included_rent', 'is_active', 'description'
        )
        widgets = {
            'description': forms.Textarea
        }


class EditPhotoForm(forms.ModelForm):
    ADD = 'A'
    DELETE = 'D'
    NONE = 'N'
    ACTION_CHOICES = (
        (ADD, 'Add'),
        (DELETE, 'Delete'),
        (NONE, 'NONE'),
    )
    action = forms.ChoiceField(choices=ACTION_CHOICES)

    class Meta:
        model = DomicilePhoto
        fields = (
            'photo_url',
        )
        widgets = {
            'photo_url': forms.FileInput()
        }


class NoValidationFormSet(BaseFormSet):
    def clean(self):
        # Perform no validation
        return

EditPhotoFormSet = formset_factory(EditPhotoForm, extra=1, formset=NoValidationFormSet)


class CreateUserForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label="Confirm password", max_length=20, widget=forms.PasswordInput
    )

    STUDENT_CHOICES = (
        ('Y', 'Yes, I am a student.'),
        ('N', 'No, I am a landlord.'),
    )

    student_account = forms.ChoiceField(choices=STUDENT_CHOICES, label='Are you a student?')

    class Meta:
        model = RegisteredUser
        fields = (
            'first_name', 'last_name', 'date_of_birth', 'physical_address', 'city', 'state', 'zip_code', 'phone_number',
            'email', 'username', 'password'
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'password': forms.PasswordInput
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = RegisteredUser
        fields = (
            'first_name', 'last_name', 'date_of_birth', 'physical_address', 'city', 'state', 'zip_code', 'phone_number',
            'bio', 'profile_picture', 'email', 'username'
        )
        widgets = {
            'bio': forms.Textarea,
            'first_name': forms.TextInput(attrs={'class':"input col form-control", "disabled":"disabled"}),
            'last_name': forms.TextInput(attrs={'class':"input col form-control", "disabled":"disabled"}),
            'date_of_birth': forms.TextInput(attrs={'class':"input col form-control", "disabled":"disabled"}),
            'physical_address': forms.TextInput(attrs={'class':"input col form-control", "disabled":"disabled"}),
            'city': forms.TextInput(attrs={'class':"input col form-control", "disabled":"disabled"}),
            'state': forms.TextInput(attrs={'class':"input col form-control", "disabled":"disabled"}),
            'email': forms.TextInput(attrs={'class':"input col form-control", "disabled":"disabled"}),
            'username': forms.TextInput(attrs={'class':"input col form-control", "disabled":"disabled"}),
            'zip_code': forms.TextInput(attrs={'class':"input col form-control", "disabled":"disabled"}),
            'phone_number': forms.TextInput(attrs={'class':"input col form-control", "disabled":"disabled"})
        }


class ForgotPasswordForm(forms.Form):
    email = forms.CharField(label="Email", max_length=20)
