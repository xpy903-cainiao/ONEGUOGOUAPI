from django.urls import path
from goodsapp.views import GoodsCart
app_name = 'goodsapp'
from mainapp.views import AddrView

urlpatterns = [
    path('goodscart/',GoodsCart.as_view(),name='goodscart'),
    path('addr/',AddrView.as_view(),name='addr')
]