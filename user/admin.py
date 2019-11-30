from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('추가 필드', {'fields': (
            'img_profile',
        )}),
    ) + BaseUserAdmin.fieldsets
