from io import BytesIO

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from mainapp.models import OneGuoCity
from api.citys import OneGuoCitySerializer


def citys_api():
    data = OneGuoCity.objects.all()
    datas = OneGuoCitySerializer(data, many=True)
    content = JSONRenderer().render(datas.data)
    buffer = BytesIO(content)
    text = JSONParser().parse(buffer)
    return text
