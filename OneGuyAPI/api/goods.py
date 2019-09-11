from rest_framework import serializers,viewsets
from goodsapp.models import GoodsModelEntity,Goods_cartModelEntity
from userapp.models import OneGuoUser,OneGuoAddress,
from orderapp.models import OrderModel,OrderDetailModel

class GoodsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsModelEntity
        fields = '__all__'


class OneGuoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneGuoUser
        fields = '__all__'

class Goods_cartModelSerializer(serializers.ModelSerializer):
    goods_id = GoodsModelSerializer()
    user_id = OneGuoUserSerializer()

    class Meta:
        model = Goods_cartModelEntity
        fields = '__all__'

class OneGuoAddressSerializer(serializers.ModelSerializer):
    user_id = OneGuoUserSerializer()
    class Meta:
        model = OneGuoAddress
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_user_id = OneGuoUserSerializer()
    class Meta:
        model = OrderModel
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    order_id = OrderSerializer()
    order_goods_id = GoodsModelSerializer()
    class Meta:
        model = OrderDetailModel
        fields = '__all__'




class GoodsApiView(viewsets.ModelViewSet):
    queryset = GoodsModelEntity.objects.all()
    serializer_class = GoodsModelSerializer

class Goods_cartApiView(viewsets.ModelViewSet):
    queryset = Goods_cartModelEntity.objects.all()
    serializer_class = Goods_cartModelSerializer

class OneGuoAddressApiView(viewsets.ModelViewSet):
    queryset = OneGuoAddress.objects.all()
    serializer_class = OneGuoAddressSerializer

class OrderDetailApiView(viewsets.ModelViewSet):
    queryset = OrderDetailModel.objects.all()
    serializer_class = OrderDetailSerializer

