from django.contrib import admin
from .models import Users, Profile

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('f', 'i','o','contractid', 'date','info')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('contractid', 'balance', 'last_trans', 'info')