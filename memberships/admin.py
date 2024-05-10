from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Utiliza el 'email' en lugar de 'username' para ver lo usuarios en ese orden
    ordering = ('email', )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    # Configuracion de formulario para registrar y editar
    fieldsets = (
        (None, {'fields': ('email','password','health_details', 'preferred_activities')}),
        ('Permissions',{'fields': ('is_active','is_staff','is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)
