import requests
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from families.models import FamilyGroup, Invitations
from .models import *
from django.contrib.auth.models import Group
from .forms import *

def accept_group_invite(request, token):

    invitation = get_object_or_404(models.invitation, token=token)

    return render(request, '/accounts/signup.html', locals())

class AddUser(CreateView):
    form_class = AddUserMultiForm
    template_name = 'accounts/addUser.html'

    def form_valid(self, form):
        user = form['user'].save()
        profile = form['profile'].save(commit=False)
        profile.user = User.objects.get(username= user.username)
        profile.save()

        token = self.request.GET.get('token')
        if token:
            invitation = Invitations.objects.get(token=token)
            group = invitation.group
            group.user_set.add(user)

        return HttpResponseRedirect(reverse('home'))


class UpdateProfile(UpdateView):
    model = UserProfile
    fields = ['profile_pic', 'bio', 'twitter', 'facebook', 'snapchat']
    template_name = 'accounts/update_profile.html'

class ProfileDetail(DetailView):
    model = User
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super(ProfileDetail, self).get_context_data(**kwargs)
        context['group_list'] = Group.objects.filter(user=self.kwargs['pk'])
        return context
