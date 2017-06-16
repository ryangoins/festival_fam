from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from families.models import FamilyGroup
from .models import *
from django.contrib.auth.models import Group
from .forms import *

class AddUser(CreateView):
    form_class = AddUserMultiForm
    template_name = 'accounts/addUser.html'

    def form_valid(self, form):
        user = form['user'].save()
        profile = form['profile'].save(commit=False)
        profile.user = User.objects.get(username= user.username)
        profile.save()
        return HttpResponseRedirect(reverse('home'))

class UpdateProfile(UpdateView):
    model = UserProfile
    fields = ['profile_pic','user', 'bio', 'twitter', 'facebook', 'snapchat']
    template_name = 'accounts/update_profile.html'

class ProfileDetail(DetailView):
    model = UserProfile
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super(ProfileDetail, self).get_context_data(**kwargs)
        self.user = get_object_or_404(User, username=self.kwargs['username'])
        context['group_list'] = Group.objects.filter(user=self.user)
        return context
