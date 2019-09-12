from io import BytesIO

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from api.goods import Goods_cartModelSerializer, GoodsModelSerializer, OrderSerializer, OrderDetailSerializer
from goodsapp.models import Goods_cartModelEntity, GoodsModelEntity
from orderapp.models import OrderModel, OrderDetailModel

from django.views import View

class Goodscart_Api_View(View):
    def get(self,request):
        data = Goods_cartModelEntity.objects.all()
        datas = Goods_cartModelSerializer(data, many=True)
        return JsonResponse(datas.data, safe=False)


class Goods_Api_View(View):
    # def get(self, request):
    #     data = GoodsModelEntity.objects.all()
    #     serialize = GoodsModelSerializer(data, many=True)
    #     return JsonResponse(serialize.data, safe=False)

    def get(self,request):
        goods_name = GoodsModelEntity.objects.get('goods_name')
        serialize = GoodsModelSerializer(goods_name)
        return JsonResponse(serialize.data, safe=False)

class Order_Api_View(View):
    def get(self, request):
        data = OrderModel.objects.all()
        serialize = OrderSerializer(data, many=True)
        content = JSONRenderer().render(serialize.data)
        buffer = BytesIO(content)
        text = JSONParser().parse(buffer)
        return JsonResponse(text, safe=False)


class OrderDetail_Api_View(View):
    def get(self, request):
        data = OrderDetailModel.objects.all()
        serialize = OrderDetailSerializer(data, many=True)
        content = JSONRenderer().render(serialize.data)
        buffer = BytesIO(content)
        text = JSONParser().parse(buffer)
        return JsonResponse(text, safe=False)
