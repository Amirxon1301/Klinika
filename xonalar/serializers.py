from rest_framework import serializers
from .models import *

class XonaSerializer(serializers.Serializer):
    class Meta:
        model = Xona
        fields = '__all__'

class JoylashtirishSerializer(serializers.Serializer):
    class Meta:
        model = Joylashtirish
        fields = '__all__'