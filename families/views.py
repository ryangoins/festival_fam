from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from . import models
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
