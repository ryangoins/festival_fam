from django.contrib import admin

# Register your models here.
from .models import Group, Membership

class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1

class GroupAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)

admin.site.register(Group, GroupAdmin)
admin.site.register(Membership)
