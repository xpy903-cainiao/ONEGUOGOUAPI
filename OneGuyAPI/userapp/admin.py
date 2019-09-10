from django.contrib import admin

# Register your models here.
from .models import OneGuoUser,OneGuoAddress


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

class OneGuoAddressAdmin(admin.ModelAdmin):
    list_display = ('user_id','user_addr','addr_state','user_name','phone')

admin.site.register(OneGuoUser, OneGuoUserAdmin)
admin.site.register(OneGuoAddress, OneGuoAddressAdmin)