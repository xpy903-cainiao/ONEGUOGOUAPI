from rest_framework import serializers, viewsets
from mainapp.models import OneGuoCity


# 序列化
class OneGuoCitySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = OneGuoCity
        fields = ('city_id', 'city_name', 'is_hot', 'py_name')


# API视图类
class OneGuoCityApiView(viewsets.ModelViewSet):
    queryset = OneGuoCity.objects.all()
    serializer_class = OneGuoCitySerializer
