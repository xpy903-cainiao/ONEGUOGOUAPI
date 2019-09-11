from rest_framework import serializers,viewsets
from goodsapp.models import GoodsModelEntity,Goods_cartModelEntity,Category
from userapp.models import OneGuoUser,OneGuoAddress
from orderapp.models import OrderModel,OrderDetailModel,OneGuoComment
from mainapp.models import OneGuoCity,Navigationmodel,NavigationInfomodel


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


class OneGuoCommentSerializer(serializers.ModelSerializer):
    order_id = OrderSerializer()
    user_id = OneGuoUserSerializer()

    class Meta:
        model = OneGuoComment
        fields = '__all__'


class OneGuoCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = OneGuoCity
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NavigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navigationmodel
        fields = '__all__'


class NavigationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationInfomodel
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


class OneGuoCommentApiView(viewsets.ModelViewSet):
    queryset = OneGuoComment.objects.all()
    serializer_class = OneGuoCommentSerializer


class OneGuoCityApiView(viewsets.ModelViewSet):
    queryset = OneGuoCity.objects.all()
    serializer_class = OneGuoCitySerializer


class CategoryApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NavigationApiView(viewsets.ModelViewSet):
    queryset = Navigationmodel.objects.all()
    serializer_class = NavigationSerializer


class NavigationInfoApiView(viewsets.ModelViewSet):
    queryset = NavigationInfomodel.objects.all()
    serializer_class = NavigationInfoSerializer