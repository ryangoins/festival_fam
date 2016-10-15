from django.contrib import admin

# Register your models here.
from .models import Event, Restrictions, Address


class EventRestrictionsInLine(admin.StackedInline):
    model = Restrictions
    can_delete = False

class EventAddressInLine(admin.StackedInline):
    model = Address
    can_delete = False

class EventAdmin(admin.ModelAdmin):
    inlines = [EventRestrictionsInLine, EventAddressInLine,]

admin.site.register(Event, EventAdmin,)
