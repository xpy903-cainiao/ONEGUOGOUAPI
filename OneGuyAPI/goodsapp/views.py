from django.shortcuts import render
from django.views.generic.base import View
from api_view import goods_api
from django.http import HttpResponse


class GoodsCart(View):
    def get(self,request):
        print('hhh')
        return render(request,'shopcart.html',locals())

    def post(self,request):
        pass


