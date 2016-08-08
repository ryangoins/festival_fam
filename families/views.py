from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test

from . import models
from families.forms import CreateGroupForm
# Create your views here.

@login_required
def group_detail(request, pk):
    group = get_object_or_404(models.FamilyGroup, pk=pk)
    members = models.User.objects.filter(familygroup=pk)
    user = request.user
    #if request.user.id in members.user.id:
    if user.is_authenticated() and user in members:
        return render(request, 'families/group_detail.html', {'group': group,
                                                            'members': members})
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
@login_required
def create_group(request):

    if request.method == "POST":
        form = CreateGroupForm(request.POST)
        user = request.user
        if form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            new_group = form.save(commit=False)
            new_group.created_at = timezone.now()
            new_group.save()
            form.save_m2m()
            new_membership = models.Membership.objects.create(user=user, group=new_group, date_joined=timezone.now(), )
            new_membership.save()
            return HttpResponseRedirect(reverse('families:detail', args=(new_group.pk,)))
    else:
        form = CreateGroupForm()

    return render(request, 'families/create_group.html', {'form': form})
