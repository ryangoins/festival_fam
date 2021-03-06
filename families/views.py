import calendar
import hashlib
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.core.urlresolvers import reverse
from datetime import date, datetime, timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test
from django_tables2 import RequestConfig
from families.tables import MealTable
from . import models
from todo.models import List
from festivals.models import Event
from families.models import FamilyGroup, Meal, Ingredient, Post, Invitations
from accounts.models import UserProfile
from django.contrib.auth.models import Group
from families.forms import AddGroupMultiForm, CreateMealForm, CreateIngredientForm, CreatePostForm, CreateInviteForm
from django.forms import formset_factory, modelformset_factory
from django.template.loader import render_to_string

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

        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = CreatePostForm(request.POST, prefix='post')
            invite_form = CreateInviteForm(request.POST, prefix='invite')
            # check whether it's valid:
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.group = Group.objects.get(pk=group_pk)
                new_post.created_at = datetime.now()
                new_post.user = request.user
                new_post.save()

            elif invite_form.is_valid():
                new_invite = invite_form.save(commit=False)
                new_invite.invitationid = 1
                new_invite.group = Group.objects.get(pk=group_pk)
                new_invite.created_at = datetime.now()
                new_invite.token = hashlib.sha1(b'new_invite.email').hexdigest()
                new_invite.save()

                email = EmailMessage(
                    'You were invited to a festival fam',
                    'Join the new_invite.group festival fam <a href="https://localhost:8000/signup?token=new_invite.token">https://localhost:8000/signup?token=new_invite.token</a>',
                    'ryan.c.goins@gmail.com',
                    [new_invite.email],
                    headers = {'Reply-To': 'ryan.c.goins@gmail.com' }
                )

                email.send()

                return HttpResponseRedirect(reverse('families:detail', args=(group_pk,)))

        # if a GET (or any other method) we'll create a blank form
        else:
            #the days tuple here is passed to the form and loaded as the choices for the day field
            form = CreatePostForm(prefix='post')
            invite_form = CreateInviteForm(prefix='invite')

        posts = models.Post.objects.filter(group_id=group_pk).order_by('-created_at')

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
    #list = get_object_or_404(List, group_id=group_pk)
    members = models.User.objects.filter(groups=group)

    user = request.user
    profile = user.userprofile

    family = FamilyGroup.objects.get(group_id=group_pk)
    festival = Event.objects.get(pk=family.event_id)
    first_day = festival.start_date
    last_day = festival.end_date
    festival_days = []
    all_meals = []

    while first_day <= last_day:

        festival_days.append(first_day.strftime("%A"))
        first_day += timedelta(days=1)

    for day in festival_days:
        meals = models.Meal.objects.filter(group_id=group_pk).filter(day=day)
        days_meals =[day,"","",""]
        days_meals.append(day)
        for meal in meals:
            if meal.time == "Breakfast":
                days_meals[1] = meal
            elif meal.time == "Lunch":
                days_meals[2] = meal
            elif meal.time == "Dinner":
                days_meals[3] = meal
        all_meals.append(days_meals)

    if user.is_authenticated() and user in members:
        return render(request, 'families/meal_list.html', {"festival_days": festival_days, "all_meals": all_meals, "group": group, "members": members})
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
    Ingredients = models.Ingredient.objects.filter(meal_id=meal_pk)
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
        FamilyGroup.create_days()
        return HttpResponseRedirect(reverse('families:detail', args=(group.pk,)))

def create_meal(request , group_pk):


    group = get_object_or_404(models.Group, pk=group_pk)
    members = models.User.objects.filter(groups=group)
    family = FamilyGroup.objects.get(group_id=group_pk)
    festival = Event.objects.get(pk=family.event_id)
    first_day = festival.start_date
    last_day = festival.end_date
    festival_days = []

    #Determines what days the festival is active in order to create options for the meal form.
    #This should probably be a new table associated with the festival itself, but working and launched
    #is better than not working and not launched

    while first_day <= last_day:
        festival_days.append(first_day.strftime("%A"))
        first_day += timedelta(days=1)

    festival_days_tuple = tuple((x, x) for x in festival_days)

    CreateIngredientFormset = modelformset_factory(Ingredient, fields=('name', 'unit', 'amount'))

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateMealForm(request.POST, days=festival_days_tuple)
        ingredient_forms = CreateIngredientFormset(request.POST)
        # check whether it's valid:
        #add ingredient_forms.is_valid() to the if statement to get ingredients back
        if form.is_valid():
            new_meal = form.save(commit=False)
            new_meal.group = Group.objects.get(pk=group_pk)
            new_meal.created_at = datetime.now()
            new_meal.created_by = request.user
            new_meal.save()

            #iterate through each form, associate it with the current meal, save
            # for ingredient_form in ingredient_forms:
            #     new_ingredient = ingredient_form.save(commit=False)
            #     new_ingredient.meal = new_meal
            #     new_ingredient.save()

            return HttpResponseRedirect(reverse('families:meal_list', args=(group_pk,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        #the days tuple here is passed to the form and loaded as the choices for the day field
        form = CreateMealForm(days=festival_days_tuple)
        #the queryset parameter sets a blank form rather than loading the existing data
        ingredient_forms = CreateIngredientFormset(queryset=Ingredient.objects.none())

    return render(request, 'families/create_meal.html', {'form': form, 'group_pk': group_pk, 'group': group, 'ingredient_forms': ingredient_forms, 'members': members } )

class CreateIngredient(CreateView):
    model = Ingredient
    fields = ('name', 'amount', 'unit',)
    template_name = 'families/meal_detail.html'
