from django import forms
from collections import OrderedDict
from django.forms import ModelForm
from betterforms.multiform import MultiModelForm
from families.models import FamilyGroup, Ingredient, Meal, Post
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

class CreateMealForm(ModelForm):

    class Meta:
        model = Meal
        fields = ('name', 'serving_size', 'time', 'day', 'instructions' )
        labels = { "instructions": "Recipe", "name": "Meal Name"
        }

    def __init__(self,*args,**kwargs):
        days = kwargs.pop('days')
        super(CreateMealForm,self).__init__(*args,**kwargs)
        self.fields['day'] = forms.ChoiceField(choices=days)

class CreateIngredientForm(ModelForm):

    class Meta:
        model = Ingredient
        fields = ('name', 'unit', 'amount',)
        labels = { "name": "Ingredient Name"}

class CreatePostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('post',)


###### VEHICLE FORMS #######
