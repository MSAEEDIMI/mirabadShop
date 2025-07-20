from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from .forms import UserChangeForm,UserCreationForm

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    ordering = ['date_joined']
    list_display = ['first_name', 'last_name', 'is_staff']
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        (_('اطلاعات شخصی'), {'fields': ('first_name', 'last_name')}),
        (_('دسترسی‌ها'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('تاریخ‌ها'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone','first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ['phone','first_name','last_name']
