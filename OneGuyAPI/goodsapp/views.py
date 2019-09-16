from django.shortcuts import render
from django.views.generic.base import View
from api_view import goods_api
from django.http import HttpResponse


class GoodsCart(View):
    def get(self,request,**kwargs):
        return render(request,'shopcart.html',locals())

    def post(self,request):
        status = request.POST.get('is_active')
        if not status:
            return render(request,'login.html',locals())
        name = request.POST.get('user_id',None)
        goods_id = request.POST.get('goods_id',None)
        count = request.POST.get('goods_count')
        return render(request,'shopcart.html',locals())




