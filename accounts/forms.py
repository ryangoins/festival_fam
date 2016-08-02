from django import forms
from collections import OrderedDict
from django.forms import ModelForm
from betterforms.multiform import MultiModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import *

class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('userName','bio', 'profile_pic', 'sex', 'phone_num', 'twitter', 'facebook', 'snapchat')


class AddUserMultiForm(MultiModelForm):
    form_classes = OrderedDict((
        ('user', UserCreationForm),
        ('profile', ProfileForm),
    ))

# Custom Loginform for use with wordpress
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
