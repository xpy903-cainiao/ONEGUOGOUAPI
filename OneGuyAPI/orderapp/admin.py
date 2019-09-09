from django.contrib import admin
from .models import OrderModel


# Register your models here.


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order_user_id', 'order_price', 'order_time', 'order_state', 'address_id')


admin.site.register(OrderModel,OrderModelAdmin)