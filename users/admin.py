from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'confirmation_code')
    fieldsets = UserAdmin.fieldsets + (
        ('Подтверждение', {'fields': ('confirmation_code',)}),
    )
