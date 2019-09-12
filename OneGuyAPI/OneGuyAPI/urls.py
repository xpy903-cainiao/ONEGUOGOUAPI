"""OneGuyAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from api import api_router
from userapp.views import LoginView

from django.urls import path, include
from goodsapp import views
from api_view import goods_api
from django.conf.urls.static import static
from django.conf import settings

from api import api_router

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.index,name=''),
<<<<<<< HEAD
    path('api/',include(api_router.urls)),
    path('goodsapi/',goods_api.Goods_Api_View.as_view(),name='goodsapi'),
    path('goodscartapi/',goods_api.Goodscart_Api_View.as_view(),name='goodscartapi'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
=======

    path('api/', include(api_router.urls)),
    path('user/', include('userapp.urls', namespace='userapp')),
    path('city/', include('mainapp.urls',namespace='city')),
]
>>>>>>> 655a439f66c130bd3f6a798490be3ba05a80f695
