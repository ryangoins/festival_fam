from django.db import models
from django.contrib.auth.models import User, Group
from festivals.models import Event
#This model represents a group of users that we call a "festival fam".

class FamilyGroup(models.Model):
    group = models.OneToOneField(Group, related_name="familygroup")
    created_at = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event, related_name="event")
    description = models.TextField(blank=True, default='')
    invite_reason = models.CharField(default='', blank=True, max_length=64)

    class Meta:
        verbose_name_plural = "groups"
