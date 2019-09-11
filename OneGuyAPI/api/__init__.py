from rest_framework import routers
from api import goods
api_router = routers.DefaultRouter()

api_router.register('goods',goods.GoodsApiView)
api_router.register('goodscart',goods.Goods_cartApiView)
api_router.register('address',goods.OneGuoAddressApiView)
api_router.register('orderdetail',goods.OrderDetailApiView)
api_router.register('comment',goods.OneGuoCommentApiView)
api_router.register('city',goods.OneGuoCityApiView)
api_router.register('category',goods.CategoryApiView)
api_router.register('nav',goods.NavigationApiView)
api_router.register('navinfo',goods.NavigationInfoApiView)
