from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


# class CustomUserAdmin(UserAdmin):
#     search_fields = ('email',)
#     list_display = ('email', 'is_staff', 'is_active',)
#     list_filter = ('email', 'is_staff', 'is_active',)
#     filter_horizontal = ('groups', 'user_permissions',)
#
#     class Meta:
#         model = User


# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone')
    list_filter = ['country']
    search_fields = ('email', 'phone')
