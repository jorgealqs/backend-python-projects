from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'username',
        'email',
        'gender',
        'identification_number',
        'country',
        'is_staff'
    )
    search_fields = ('email', 'identification_number', 'country')
    ordering = ('email',)
    list_filter = ('is_staff', 'is_superuser', 'gender', 'country')

    fieldsets = (
        (
            None,
            {'fields': (
                'identification_number', 'username', 'email', 'password'
            )}
        ),
        ('Personal Info', {'fields': (
            'gender', 'address', 'country'
        )}),
        ('Permissions', {'fields': (
            'is_active', 'is_staff', 'is_superuser', 'groups',
            'user_permissions'
        )}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'gender',
                'identification_number', 'address', 'country',
                'is_staff', 'is_active')}),
    )
