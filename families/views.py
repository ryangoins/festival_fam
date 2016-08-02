from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from . import models
# Create your views here.
def group_detail(request, pk):
    group = get_object_or_404(models.Group, pk=pk)
    members = models.Membership.objects.filter(group_id=pk)
    #if request.user.id in members.user.id:
    return render(request, 'families/group_detail.html', {'group': group,
                                                          'members': members})
    #else:
    #    return render(request, 'families/public_group_detail.html', {'group': group})

#check the username in an url slug and ensure it's the same as the logged in user

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

def private_groups(request):
    username = request.user.get_username()
    return render(request, 'families/private_groups.html', {'username': username} )
