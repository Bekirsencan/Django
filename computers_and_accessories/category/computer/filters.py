from django_filters import rest_framework as filters

from .models import Computer


class ComputerFilter(filters.FilterSet):
    class Meta:
        model = Computer
        fields = ['product_name', 'product_brand', 'cpu', 'operating_system']
