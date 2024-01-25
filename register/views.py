from django.shortcuts import render

from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework.views import APIView

class BemorlarAPI(APIView):
    def get(self, request):
        bemorlar = Bemor.objects.order_by("-id")
        qidiruv = request.query_params.get("qidiruv")
        if qidiruv is not None:
            bemorlar = bemorlar.filter(ism=qidiruv
                                       ) | bemorlar.filter(tel=qidiruv)
        serializer = BemorSerializer(bemorlar, many=True)

        return Response(serializer.data)
