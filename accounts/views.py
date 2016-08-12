from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from .models import *
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
