from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=650)
    image = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=15)
    info = models.CharField(max_length=255)
    discount = models.FloatField()
