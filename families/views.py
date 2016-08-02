from django.shortcuts import get_object_or_404, render

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

def group_list(request, username):
    username = get_object_or_404(models.User, username=username)
    groups = models.Group.objects.filter(user=username)

    return render(request, 'families/group_list.html', {'username': username,
                                                        'groups': groups})
