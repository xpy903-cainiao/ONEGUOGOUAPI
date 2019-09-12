from django.contrib import admin
from goodsapp import models
from .models import Category

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


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','code','picture_url','grade','parent_id')
    fields = ('name','code','picture_url','parent','grade')
    search_fields = ('code','name')
    list_per_page = 20


admin.site.register(models.GoodsModelEntity,GoodsModelAdmin)
admin.site.register(models.Goods_cartModelEntity,Goods_cartModelAdmin)
admin.site.register(Category,CategoryAdmin)