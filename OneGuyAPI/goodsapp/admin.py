from django.contrib import admin
from goodsapp import models

# Register your models here.
class GoodsModelAdmin(admin.ModelAdmin):
    list_display = ('goods_type','goods_type_info',
                    'goods_name','goods_info',
                    'goods_price','super_price',
                    'product_address','info_page',
                    'goods_sale','goods_have',
                    'info_id','type_id',
                    'goods_img','is_detail')
class Goods_cartModelAdmin(admin.ModelAdmin):
    list_display = ('user_id','goods_id','goods_count','is_choice')

admin.site.register(models.GoodsModelEntity,GoodsModelAdmin)
admin.site.register(models.Goods_cartModelEntity,Goods_cartModelAdmin)