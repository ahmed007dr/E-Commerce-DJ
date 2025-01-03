from django import forms
from django.contrib.auth.forms import UserCreationForm # form to create user
from django.contrib.auth.models import User


class SignupForm(UserCreationForm): # hash password
    class Meta:
        models = User  # default django
        fields = ['username','email','password1','password2']



# we can make form with out models.py <<<<<<<<< >>>>>>>>>>>>>>>
class UserActivateForm(forms.Form): 
    code = forms.CharField(max_length=10)