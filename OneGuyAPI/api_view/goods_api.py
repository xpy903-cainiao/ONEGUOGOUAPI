from io import BytesIO

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from api.goods import Goods_cartModelSerializer, GoodsModelSerializer
from goodsapp.models import Goods_cartModelEntity, GoodsModelEntity

from django.views import View

def goods_api():
    data = GoodsModelEntity.objects.all()
    datas = GoodsModelSerializer(data,many=True)
    content = JSONRenderer().render(datas.data)
    buffer = BytesIO(content)
    text = JSONParser().parse(buffer)
    return text

def goods_cart_api():
    data = Goods_cartModelEntity.objects.all()
    datas = Goods_cartModelSerializer(data,many=True)
    content = JSONRenderer().render(datas.data)
    buffer = BytesIO(content)
    text = JSONParser().parse(buffer)
    return text

class Goods_Api_View(View):
    def get(self,request):
        data = GoodsModelEntity.objects.all()
        serialize = GoodsModelSerializer(data,many=True)
        content = JSONRenderer().render(serialize.data)
        buffer = BytesIO(content)
        text = JSONParser().parse(buffer)
        return JsonResponse(text,safe=False)