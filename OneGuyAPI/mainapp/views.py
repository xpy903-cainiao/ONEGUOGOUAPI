from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import render
from django.views import View

from api_view import citys_api


# Create your views here.
class CityView(View):
    def get(self, request):
        test3 = citys_api.citys_api()
        return render(request, 'city.html', locals())
# def index(request):
#
#     return render(request, 'index.html', locals())
