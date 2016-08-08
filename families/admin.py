from django.contrib import admin

# Register your models here.
from .models import FamilyGroup, Membership
from django_comments.models import Comment

class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1

class GroupAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)



admin.site.register(FamilyGroup, GroupAdmin)
admin.site.register(Membership)
