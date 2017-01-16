from django.db import models
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
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

    def get_absolute_url(self):
        return reverse('families:detail', kwargs={'group_pk': self.group_id})

class Meal(models.Model):
    name = models.CharField(blank=True, default='', max_length=255)
    time_choices = (('Breakfast', 'Breakfast'),('Lunch', 'Lunch'), ('Dinner', 'Dinner'))
    time = models.CharField(blank=True, max_length=255, default='', choices=time_choices,)
    day = models.CharField(default='', blank=True, max_length=255, choices=(),)
    group = models.ForeignKey(Group, related_name="meal_group", null=True)
    serving_size = models.IntegerField(blank=True, default='')
    instructions = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="meal_created_by")

    def __str__(self):
        return self.name

class FestivalDay(models.Model):
    familygroup = models.ForeignKey(FamilyGroup, related_name="Day")
    weekday = models.CharField(blank=True, default='', max_length=255)
    date = models.DateTimeField()
    breakfast = models.OneToOneField(Meal, related_name="Breakfast")
    lunch = models.OneToOneField(Meal, related_name="Lunch")
    dinner = models.OneToOneField(Meal, related_name="Dinner")

class Ingredient(models.Model):
    name = models.CharField(blank=True, default='', max_length=255)
    meal = models.ForeignKey(Meal, default='', related_name="ingredient_meal")
    amount = models.IntegerField(blank=True, default='')
    unit_choices = (('g', 'Grams'), ('oz', 'Ounces'))
    unit = models.CharField(default='', blank=True, max_length=10, choices=unit_choices,)

class Post(models.Model):
    post = models.TextField(blank=True, default='')
    url = models.URLField¶()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="post_created_by")


class Vehicle(models.Model):
    driver = models.OneToOneField(User, default='', related_name="vehicle_driver")
    group = models.OneToOneField(Group, default='', related_name="vehicle_group")
    passengers = models.ForeignKey(User, default='', related_name="vehicle_passengers")
    vehicle_make = models.CharField(default='', max_length=255)
    vehicle_model = models.CharField(default='', max_length=255)
    departure_location_name = models.CharField(blank=True, default='', max_length=255)
    departure_street = models.CharField(blank=True, default='', max_length=255)
    departure_city = models.CharField(blank=True, default='', max_length=255)
    departure_state = models.CharField(blank=True, default='', max_length=2)
    departure_zip = models.IntegerField(blank=True, default='')
    parking_pass = models.BooleanField(default=False)
