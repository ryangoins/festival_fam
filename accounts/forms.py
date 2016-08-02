from django import forms
from collections import OrderedDict
from django.forms import ModelForm
from betterforms.multiform import MultiModelForm
from django.contrib.auth.forms import UserCreationForm
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
