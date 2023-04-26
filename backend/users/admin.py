from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import Subscription, User


class CustomUserAdmin(UserAdmin):
    """Кастомная админка для модели User."""
    search_fields = ('email', 'username')
    list_filter = ('email', 'username')
    ordering = ('pk',)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'author'
    )
    search_fields = ('user__username', 'author__username')


admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
