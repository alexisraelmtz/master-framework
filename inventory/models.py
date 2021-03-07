from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=650)
    image = models.ImageField(upload_to="media/")
    # height_field=..., width_field=...


class Offer(models.Model):
    code = models.CharField(max_length=15)
    info = models.CharField(max_length=255)
    discount = models.FloatField()
