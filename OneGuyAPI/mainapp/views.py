from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import render
from django.views import View

from api_view import citys_api

class IndexView(View):
    def get(self,request):
        return render(request,'index_m.html',locals())


# Create your views here.
class CityView(View):
    def get(self, request):
        test3 = citys_api.citys_api()
        return render(request, 'city.html', locals())

class AddrView(View):
    def get(self,request):
        return render(request,'Addr.html',locals())