from os import error
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.exceptions import ValidationError
from django.forms import fields
# from accounts.models import Accounts

class UserRegistrationForm(UserCreationForm):
    first_name= forms.CharField()
    last_name= forms.CharField()
    email = forms.EmailField()
    def __init__(self, *args, **kwargs) -> None:
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email):
            raise ValidationError(("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']