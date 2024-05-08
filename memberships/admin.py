from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('health_details', 'preferred_activities')}),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)
