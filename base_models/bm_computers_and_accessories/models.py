from django.db import models
from department.models import Department


class BaseModelComputerAndAccessories(Department):
    category_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_brand = models.CharField(max_length=100)

    class Meta:
        abstract = True
