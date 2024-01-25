from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError

class BemorSerializer(serializers.Serializer):
    class Meta:
        model = Bemor
        fields = '__all__'


class YollanmaSerializer(serializers.Serializer):
    class Meta:
        model = Yollanma
        fields = '__all__'