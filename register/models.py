from django.db import models

class Bemor(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=40)
    manzil = models.CharField(max_length=50)

class Yollanma(models.Model):
    nom = models.CharField(max_length=40)
    narx = models.PositiveIntegerField()
    qayerga = models.CharField(max_length=50)


