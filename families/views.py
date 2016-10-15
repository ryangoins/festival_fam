from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from datetime import date, timedelta as td
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test

from . import models
from todo.models import List
from festivals.models import Event
from families.models import FamilyGroup, Meal, Ingredient
from accounts.models import UserProfile
from django.contrib.auth.models import Group
from families.forms import AddGroupMultiForm, CreateMealForm

# Create your views here.

@login_required
def group_detail(request, group_pk=None):

    #turn this into a function of some sort
    group = get_object_or_404(models.Group, pk=group_pk)
    familygroup = get_object_or_404(models.FamilyGroup, group_id=group_pk)
    #list = get_object_or_404(List, group_id=group_pk)
    event = familygroup.event
    members = models.User.objects.filter(groups=group)
    user = request.user
    profile = user.userprofile

    #if request.user.id in members.user.id:
    if user.is_authenticated() and user in members:
        return render(request, 'families/group_detail.html', locals())
    elif request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home',))
    else:
        messages.add_message(request, messages.ERROR,
                                'Please login')
        return HttpResponseRedirect(reverse('accounts:login',))


def group_list(request, username):
    #for some reason if I change the username variable this doesn't work. can't figure it out.
    username = get_object_or_404(models.User, username=username)
    groups = models.Group.objects.filter(user=username)
    #compares the users pk to the pk of the user requested
    if username == request.user:
        return render(request, 'families/group_list.html', {'username': username,
                                                            'groups': groups})
    else:
        return render(request, 'families/event_list.html', {'username': username,
                                                           'groups': groups})

def meal_list(request, group_pk=None):
    #turn this into a function of some sort
    group = get_object_or_404(models.Group, pk=group_pk)
    meals = models.Meal.objects.filter(group_id=group_pk)
    #list = get_object_or_404(List, group_id=group_pk)
    members = models.User.objects.filter(groups=group)
    user = request.user
    profile = user.userprofile

    if user.is_authenticated() and user in members:
        return render(request, 'families/meal_list.html', locals())
    elif request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home',))
    else:
        messages.add_message(request, messages.ERROR,
                                'Please login')
        return HttpResponseRedirect(reverse('accounts:login',))

def meal_detail(request, group_pk=None, meal_pk=None):
    #turn this into a function of some sort
    group = get_object_or_404(models.Group, pk=group_pk)
    meal = get_object_or_404(models.Meal, pk=meal_pk)
    ingredients = models.Ingredient.objects.filter(meal_id=meal_pk)
    #list = get_object_or_404(List, group_id=group_pk)
    members = models.User.objects.filter(groups=group)
    user = request.user
    profile = user.userprofile

    if user.is_authenticated() and user in members:
        return render(request, 'families/meal_detail.html', locals())
    elif request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home',))
    else:
        messages.add_message(request, messages.ERROR,
                                'Please login')
        return HttpResponseRedirect(reverse('accounts:login',))


class CreateGroup(CreateView):
    form_class = AddGroupMultiForm
    template_name = 'families/create_group.html'

    def form_valid(self, form):
        group = form['group'].save()
        #adds user to group
        group.user_set.add(self.request.user)
        group.save()
        familygroup = form['familygroup'].save(commit=False)
        familygroup.group = Group.objects.get(name= group.name)
        familygroup.save()
        return HttpResponseRedirect(reverse('families:detail', args=(group.pk,)))

class CreateMeal(CreateView):
    form_class = CreateMealForm
    template_name = 'families/create_meal.html'

    def get_form(self, form_class):
        #Need to create a list of the days
        family = FamilyGroup.objects.get(group_id=self.kwargs['group_pk'])
        festival = Event.objects.get(pk=family.event_id)
        first_day = festival.start_date
        last_day = festival.end_date
        delta = first_day - last_day
        festival_days = []

        for day in range(delta.days + 1):
            festival_days.append(day.strftime("%A"))
            return festival_days
        #Need to add that list as an option to the form
        form = super(CreateMeal, self).get_form(form_class)
        form.fields["day"] = form.ChoiceField(choices=festival_days)
        return form


class CreateIngredient(CreateView):
    model = Ingredient
    fields = ('name', 'amount', 'unit',)
    template_name = 'families/meal_detail.html'
