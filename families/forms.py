from django import forms
from collections import OrderedDict
from django.forms import ModelForm

from families.models import Group

class CreateGroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['event', 'title', 'description']
    #create membership object between logged in user and new group
