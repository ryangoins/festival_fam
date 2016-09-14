from django import forms
from collections import OrderedDict
from django.forms import ModelForm
from betterforms.multiform import MultiModelForm
from families.models import FamilyGroup, Ingredient, Meal
from django.contrib.auth.models import Group


from .models import *

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        exclude = ('permissions',)

class FamilyGroupForm(forms.ModelForm):

    class Meta:
        model = FamilyGroup
        exclude = ('created_at','date_joined', 'invite_reason', 'group',)

class AddGroupMultiForm(MultiModelForm):
    form_classes = OrderedDict((
        ('group', GroupForm),
        ('familygroup', FamilyGroupForm),
    ))

class CreateMealForm(forms.ModelForm):

    class Meta:
        model = Meal
        exclude =('created_at', 'created_by', 'group',)

class CreateIngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ('name', 'amount', 'unit')
