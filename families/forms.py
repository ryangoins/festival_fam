from django import forms
from collections import OrderedDict
from django.forms import ModelForm

from families.models import FamilyGroup

class CreateGroupForm(forms.ModelForm):

    class Meta:
        model = FamilyGroup
        fields = ['event', 'title', 'description']
    #create membership object between logged in user and new group
