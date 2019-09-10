from io import BytesIO

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from api.goods import Goods_cartModelSerializer, GoodsModelSerializer
from goodsapp.models import Goods_cartModelEntity, GoodsModelEntity


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