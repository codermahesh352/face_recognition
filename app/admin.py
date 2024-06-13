# myapp/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User

class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    list_display = ('username', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # Add fields to be displayed when creating a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'face_encoding', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

# Register the new UserAdmin
admin.site.register(User, UserAdmin)

# Unregister the Group model from admin since we're not using it
admin.site.unregister(Group)
