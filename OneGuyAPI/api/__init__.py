from rest_framework import routers
from api import goods
api_router = routers.DefaultRouter()

api_router.register('goods',goods.GoodsApiView)
api_router.register('goodscart',goods.Goods_cartApiView)
api_router.register('address',goods.OneGuoAddressApiView)
api_router.register('orderdetail',goods.OrderDetailApiView)
