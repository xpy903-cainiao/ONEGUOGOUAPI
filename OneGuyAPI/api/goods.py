from rest_framework import serializers
from goodsapp.models import GoodsModelEntity,Goods_cartModelEntity

class GoodsModelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GoodsModelEntity
        fields = ('goods_type','goods_type_info',
                  'goods_name','goods_info',
                  'goods_price','super_price',
                  'product_address','info_page',
                  'goods_sale','goods_have',
                  'info_id','type_id',
                  'goods_img','is_detail')

class Goods_cartModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goods_cartModelEntity
        fields = ('user_id','goods_id',
                  'goods_count','is_choice')
