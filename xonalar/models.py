from django.db import models

from register.models import Bemor

class Xona(models.Model):
    qavat = models.PositiveIntegerField()
    raqam = models.PositiveIntegerField()
    sigim = models.PositiveIntegerField()
    tur = models.CharField(max_length=40)
    narx = models.PositiveIntegerField()
    bosh_joy_soni = models.PositiveIntegerField()

class Joylashtirish(models.Model):
    bemor = models.ForeignKey(Bemor, on_delete=models.CASCADE)
    xona = models.ForeignKey(Xona, on_delete=models.CASCADE)
    izoh = models.TextField(null=True, blank=True)
    kelgan_sana = models.DateField()
    ketgan_sana = models.DateField()
    yotgan_kun_soni = models.PositiveIntegerField()
    qarovchi = models.BooleanField(default=False)

