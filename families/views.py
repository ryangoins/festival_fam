from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone

from . import models
from families.forms import CreateGroupForm
# Create your views here.
def group_detail(request, pk):
    group = get_object_or_404(models.Group, pk=pk)
    members = models.Membership.objects.filter(group_id=pk)
    #if request.user.id in members.user.id:
    return render(request, 'families/group_detail.html', {'group': group,
                                                          'members': members})
def group_list(request, username):
    username = get_object_or_404(models.User, username=username)
    authd_user = request.user
    groups = models.Group.objects.filter(user=username)
    #compares the users pk to the pk of the user requested
    if username == authd_user:
        return render(request, 'families/group_list.html', {'username': username,
                                                            'groups': groups})
    else:
        return render(request, 'families/event_list.html', {'username': username,
                                                           'groups': groups})
@login_required
def create_group(request):
    
    if request.method == "POST":
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = CreateGroupForm()

    return render(request, 'families/create_group.html', {'form': form})
