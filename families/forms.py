from django import forms
from collections import OrderedDict
from django.forms import ModelForm
from betterforms.multiform import MultiModelForm
from families.models import FamilyGroup, Ingredient, Meal, Post, Invitations
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

class CreateInviteForm(forms.ModelForm):

    class Meta:
        model = Invitations
        fields = ('email',)

class AddGroupMultiForm(MultiModelForm):
    form_classes = OrderedDict((
        ('group', GroupForm),
        ('familygroup', FamilyGroupForm),
    ))

class CreateMealForm(ModelForm):

    class Meta:
        model = Meal
        fields = ('name', 'recipe_url', 'serving_size', 'time', 'day', 'instructions' )
        labels = { "instructions": "Notes", "name": "Meal Name", "recipe_url": "Link to Recipie",
                    "time": "When are you going to eat it?", "day": "Which day?"
        }

    def __init__(self,*args,**kwargs):
        days = kwargs.pop('days')
        super(CreateMealForm,self).__init__(*args,**kwargs)
        self.fields['day'] = forms.ChoiceField(choices=days)
        self.fields['recipe_url'].widget.attrs={
        'placeholder': 'http://allrecipes.com/'
        }

class CreateIngredientForm(ModelForm):

    class Meta:
        model = Ingredient
        fields = ('name', 'unit', 'amount',)
        labels = { "name": "Ingredient Name"}

class CreatePostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('post',)
        labels = { "post": ""}

    def __init__(self,*args,**kwargs):
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.fields['post'].widget.attrs={
            'class': 'post-text',
            'placeholder': 'What would you like to share with your fam?'
            }




###### VEHICLE FORMS #######
