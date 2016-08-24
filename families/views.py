from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test

from . import models
from todo.models import List
from families.models import FamilyGroup
from accounts.models import UserProfile
from django.contrib.auth.models import Group
from families.forms import AddGroupMultiForm
# Create your views here.

@login_required
def group_detail(request, group_pk=None):

    #turn this into a function of some sort
    group = get_object_or_404(models.Group, pk=group_pk)
    #list = get_object_or_404(List, group_id=pk)
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
    groups = models.FamilyGroup.objects.filter(user=username)
    #compares the users pk to the pk of the user requested
    if username == request.user:
        return render(request, 'families/group_list.html', {'username': username,
                                                            'groups': groups})
    else:
        return render(request, 'families/event_list.html', {'username': username,
                                                           'groups': groups})

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
