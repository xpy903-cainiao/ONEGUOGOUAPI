from django.contrib import admin

# Register your models here.
from .models import OneGuoUser


class OneGuoUserAdmin(admin.ModelAdmin):
    list_display = (
        'phone',
        'name',
        'gender',
        'password',
        'idcard',
        'img',
        'balance',
        'use_level',
        'is_active',
        'is_delete')
    fields = (
        'phone',
        'name',
        'gender',
        'password',
        'idcard',
        'img',
        'balance',
        'use_level',
        'is_active',
        'is_delete')
    search_fields = ('phone', 'name', 'idcard', 'is_active', 'is_delete')


admin.site.register(OneGuoUser, OneGuoUserAdmin)
