"""Users admin."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import AppUser


class MyUserAdmin(UserAdmin):
    """
    Admin back end class.

    This is for handling Django admin create user.
    """

    model = AppUser

    list_display = ['username', 'sex', 'surname', 'first_name', 'last_name',
                    'email', 'timestamp_created', 'is_active']

    search_fields = ['username']
    readonly_fields = ['reg_person']
    list_filter = ['is_active', 'is_staff', 'is_superuser',
                   'timestamp_created', 'groups', 'reg_person__sex_id']

    fieldsets = (
        (_('Personal info'), {'fields': ('username', 'password',
                              'reg_person')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
                            'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',
                                'password_changed_timestamp')}),
        (_('Groups'), {'fields': ('groups',)}),
    )

    add_fieldsets = (
        (_('Create Account'), {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'reg_person')}
         ),
    )


admin.site.register(AppUser, MyUserAdmin)
