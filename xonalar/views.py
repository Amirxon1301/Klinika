from django.shortcuts import render

# atomic transaction
from django.db import transaction

from datetime import datetime

from .models import *
from .serializers import *
from tolovlar.models import *


from rest_framework.response import Response
from rest_framework.views import APIView

class XonalarAPI(APIView):
    def get(self, request):
        xonalar = Xona.objects.all()
        qarovchisi = request.query_params.get("qarovchi")
        if qarovchisi == 'true':
            xonalar = xonalar.filter(bosh_joy_soni__gt=1)
        elif qarovchisi == 'false':
            xonalar = xonalar.filter(bosh_joy_soni__gt=0)
        serializer = XonaSerializer(xonalar, many=True)
        return Response(serializer.data)

class JoylashtirishlarAPI(APIView):
    def get(self, request):
        joylashtirishlar = Joylashtirish.objects.order_by("-id")
        holat = request.query_params.get("holat")
        if holat == 'ketgan':
            joylashtirishlar = joylashtirishlar.filter(ketish_sana_isnull=False)
        elif holat == 'ketmagan':
            joylashtirishlar = joylashtirishlar.filter(ketish_sana_isnull=True)
        serializer = JoylashtirishSerializer(joylashtirishlar, many=True)

        return Response(serializer.data)

    @transaction.atomic
    def post(self, request):
        joylashtirish = request.data
        serializer = JoylashtirishSerializer(data=joylashtirish)
        if serializer.is_valid():
            joylashtirish = serializer.save()

            bemor = Bemor.objects.get(id=joylashtirish.bemor.id)
            bemor.joylashgan = True
            bemor.save()

            xona = Xona.objects.get(id=joylashtirish.xona.id)
            if joylashtirish.qarovchi == True:
                xona.bosh_joy_soni -= 2
            else:
                xona.bosh_joy_soni -= 1
            xona.save()

            Tolov.objects.create(
                bemor = bemor,
                joylashtirish = joylashtirish,
                summa = 0
            )
            return Response(serializer.data)
        return Response(serializer.errors)

class JoylashtirishAPI(APIView):
    @transaction.atomic
    def update(self, request, pk):
        joylashtirish = Joylashtirish.objects.get(id=pk)
        serializer = JoylashtirishSerializer(joylashtirish, data=request.data)
        if serializer.is_valid():
            joylashtirish = serializer.save()

            bemor = Bemor.objects.get(id=joylashtirish.bemor.id)
            bemor.joylashgan = False
            bemor.save()

            xona = Xona.objects.get(id=joylashtirish.xona.id)
            if joylashtirish.qarovchi == True:
                xona.bosh_joy_soni += 2
            else:
                xona.bosh_joy_soni += 1
            xona.save()
            tolov = Tolov.objects.get(joylashtirish =  joylashtirish)
            d1 = datetime.strptime(datetime.today(), "%Y-%m-%d")
            d2 = datetime.strptime(joylashtirish.kelgan_sana, "%Y-%m-%d")
            farqi = d1.day - d2.day
            joylashtirish.yotgan_kun_soni = farqi
            joylashtirish.save()
            summa = xona.narx * farqi
            tolov.summa = summa
            tolov.save()

            return Response(serializer.data)
        return Response(serializer.errors)