from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="userprofile")
    bio = models.TextField(default='', blank=True)
    profile_pic = models.ImageField(default='', blank=True, upload_to='media/')
    sex_choices = (('m', 'Male'), ('f', 'Female'))
    sex = models.CharField(default='', blank=True, max_length=10, choices=sex_choices,)
    phone_num = models.CharField(default='', blank=True, max_length=30)
    twitter = models.URLField(default='', blank=True)
    facebook = models.URLField(default='', blank=True)
    snapchat = models.URLField(default='', blank=True)

    def __unicode__(self):  # __str__
        return unicode(self.user)
