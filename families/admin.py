from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
# Register your models here.
from .models import FamilyGroup, Meal
from django_comments.models import Comment


class MealInLine(admin.StackedInline):
    model = Meal
    can_delete = True
    verbose_name_plural = 'meals'

class FamilyGroupInLine(admin.StackedInline):
    model = FamilyGroup
    can_delete = False

class NewGroupAdmin(GroupAdmin):
    inlines = (FamilyGroupInLine, MealInLine,)

admin.site.unregister(Group)
admin.site.register(Group, NewGroupAdmin)
