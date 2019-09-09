from django.contrib import admin
from .models import OrderModel,OrderDetailModel
from .models import OrderModel, OneGuoComment



# Register your models here.



class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('order_id',
                    'order_user_id',
                    'order_price',
                    'order_time',
                    'order_state',
                    'address_id')


class OrderDetailModelAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order_goods_id', 'order_goods_num')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_id',
                    'order_id',
                    'comments')


admin.site.register(OrderModel, OrderModelAdmin)
admin.site.register(OrderDetailModel, OrderDetailModelAdmin)
admin.site.register(OneGuoComment, CommentAdmin)







