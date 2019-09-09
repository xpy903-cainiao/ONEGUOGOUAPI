from django.contrib import admin

# Register your models here.
from .models import OneGuoCity


class OneGuoCityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name', 'is_hot', 'py_name')
    fields = ('city_name', 'is_hot', 'py_name')
    search_fields = ('city_name', 'py_name', 'is_hot')


admin.site.register(OneGuoCity, OneGuoCityAdmin)
