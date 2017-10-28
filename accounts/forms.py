from django import forms
from collections import OrderedDict
from django.forms import ModelForm
from betterforms.multiform import MultiModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user','bio', 'profile_pic', 'sex', 'phone_num', 'twitter', 'facebook', 'snapchat')

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

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
