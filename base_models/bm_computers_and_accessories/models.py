from django.db import models


class BaseModelComputerAndAccessories(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_brand = models.CharField(max_length=100)

    class Meta:
        abstract = True

