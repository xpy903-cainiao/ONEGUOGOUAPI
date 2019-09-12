from rest_framework import serializers,viewsets
from goodsapp.models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('code','name','grade','parent','picture_url')

class CategoryAPTView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


