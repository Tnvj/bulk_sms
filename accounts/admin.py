from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Contact, Group, Message, MessageLog
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'name', 'phone_number', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'phone_number', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ['email', 'name', 'phone_number']
    ordering = ['email']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Contact)
admin.site.register(Group)
admin.site.register(Message)
admin.site.register(MessageLog)
