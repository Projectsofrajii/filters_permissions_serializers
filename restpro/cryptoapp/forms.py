from phonenumber_field.modelfields import PhoneNumberField
from restpro.cryptoapp.managers import UserManager
from restpro.cryptoapp.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

class UserCreationForm(BaseUserCreationForm):
    phoneno = forms.CharField(max_length=20, required=True, help_text='Phone number')
    email = forms.CharField(max_length=50, required=True, help_text='email number')

    objects = UserManager()
    class Meta:
        model = User
        fields = ('username', 'phoneno', 'password','email')