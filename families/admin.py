from django.contrib import admin

# Register your models here.
from .models import FamilyGroup
from django_comments.models import Comment





admin.site.register(FamilyGroup)
