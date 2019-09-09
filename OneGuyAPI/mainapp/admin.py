from django.contrib import admin

# Register your models here.

from .models import OneGuoCity, Navigationmodel, NavigationInfomodel


class OneGuoCityAdmin(admin.ModelAdmin):
    list_display = ('city_id', 'city_name', 'is_hot', 'py_name')
    fields = ('city_name', 'is_hot', 'py_name')
    search_fields = ('city_name', 'py_name', 'is_hot')


class NavigationmodelAdmin(admin.ModelAdmin):
    list_display = ('Navigation_img1', 'Navigation_name', 'Navigation_id')


class NavigationInfomodelAdmin(admin.ModelAdmin):
    list_display = ('NavigationInfo_img1', 'NavigationInfo_name', 'NavigationInfo_id', 'user_id')


admin.site.register(OneGuoCity, OneGuoCityAdmin)
admin.site.register(Navigationmodel, NavigationmodelAdmin)
admin.site.register(NavigationInfomodel, NavigationInfomodelAdmin)
