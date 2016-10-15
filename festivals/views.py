from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from datetime import date, timedelta as td
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test


from django.contrib.auth.models import Group, User
from festivals.models import Event
from families.models import FamilyGroup
from accounts.models import UserProfile

# Create your views here.
def event_info(request, group_pk, event_slug):

    #turn this into a function of some sort
    group = get_object_or_404(Group, pk=group_pk)
    familygroup = get_object_or_404(FamilyGroup, group_id=group_pk)
    #list = get_object_or_404(List, group_id=group_pk)
    members = User.objects.filter(groups=group)
    user = request.user
    profile = user.userprofile

    #if request.user.id in members.user.id:
    if user.is_authenticated() and user in members:
        return render(request, 'festivals/event_info.html', locals())
    elif request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home',))
    else:
        messages.add_message(request, messages.ERROR,
                                'Please login')
        return HttpResponseRedirect(reverse('accounts:login',))
