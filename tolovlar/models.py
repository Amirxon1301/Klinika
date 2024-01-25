from django.db import models

from register.models import Bemor, Yollanma
from xonalar.models import Joylashtirish

class Tolov(models.Model):
    bemor = models.ForeignKey(Bemor, on_delete=models.CASCADE)
    yollanma = models.ForeignKey(Yollanma, on_delete=models.CASCADE, null=True)
    joylashtirish = models.ForeignKey(Joylashtirish, on_delete=models.CASCADE, null=True)
    summa = models.PositiveIntegerField()
    tanlangan_summa = models.PositiveIntegerField()
    tolandi = models.BooleanField()
    created_sana = models.DateField()
    tolangan_sana = models.DateField(null=True, blank=True)
    turi = models.CharField(max_length=40, null=True, blank=True)
    izoh = models.TextField(null=True, blank=True)

class QoshimchaTolov(models.Model):
    tolov = models.ForeignKey(Tolov, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    summa = models.IntegerField()
    izoh = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.izoh