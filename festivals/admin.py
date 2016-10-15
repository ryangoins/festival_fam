from django.contrib import admin

# Register your models here.
from .models import Event, Restrictions


class EventRestrictionsInLine(admin.StackedInline):
    model = Restrictions
    can_delete = False

class EventAdmin(admin.ModelAdmin):
    inlines = [EventRestrictionsInLine]

admin.site.register(Event, EventAdmin,)
