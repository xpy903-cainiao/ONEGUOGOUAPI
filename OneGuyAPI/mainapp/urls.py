from mainapp import views

from django.urls import path

from .views import CityView

app_name = 'city'

urlpatterns = [
    path('citys/', CityView.as_view(), name='citys'),
]
