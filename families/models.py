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

class Meal(models.Model):
    name = models.CharField(blank=True, default='', max_length=255)
    time_choices = (('Breakfast', 'breakfast'),('Lunch', 'lunch'), ('Dinner', 'dinner'))
    time = models.CharField(blank=True, max_length=255, default='', choices=time_choices,)
    day = models.CharField(blank=True, max_length=255, default='')
    group = models.ForeignKey(Group, related_name="meal_group", null=True)
    serving_size = models.IntegerField(blank=True, default='')
    instructions = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(blank=True, default='', max_length=255)
    meal = models.ForeignKey(Meal, default='', related_name="ingredient_meal")
    amount = models.IntegerField(blank=True, default='')
    unit_choices = (('g', 'Grams'), ('oz', 'Ounces'))
    unit = models.CharField(default='', blank=True, max_length=10, choices=unit_choices,)
