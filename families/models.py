from django.db import models
from django.contrib.auth.models import User
from festivals.models import Event
#This model represents a group of users that we call a "festival fam".

class Group(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(User, through='Membership')
    event = models.ForeignKey(Event)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title


class Membership(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
