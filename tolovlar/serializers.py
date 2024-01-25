from rest_framework import serializers
from .models import *


class TolovSerializer(serializers.Serializer):
    class Meta:
        model = Tolov
        fields = '__all__'

class QoshimchaTolovlarSerializer(serializers.Serializer):
    class Meta:
        model = QoshimchaTolov
        fields = '__all__'