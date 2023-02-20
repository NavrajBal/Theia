from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'firstname', 'lastname', 'is_staff', 'is_active',)
    list_filter = ('email', 'firstname', 'lastname','is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'firstname', 'lastname', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'firstname', 'lastname', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'firstname', 'lastname')
    ordering = ('email', 'firstname', 'lastname')


admin.site.register(CustomUser, CustomUserAdmin)