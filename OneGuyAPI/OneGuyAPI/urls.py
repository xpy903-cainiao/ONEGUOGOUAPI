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
<<<<<<< HEAD
from django.urls import path,include
from api import api_router
from userapp.views import LoginView
=======
from django.urls import path, include
from goodsapp import views
from api_view.goods_api import Goods_Api_View
from api import api_router
>>>>>>> 0c60a971b1a285e8956d5dd1c207b9f20a68747f

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.index,name=''),
<<<<<<< HEAD
    path('api/',include(api_router.urls)),
    path('user/',include('userapp.urls',namespace='userapp'))

=======
    path('api/', include(api_router.urls)),
    path('city/', include('mainapp.urls')),
>>>>>>> 0c60a971b1a285e8956d5dd1c207b9f20a68747f
]
