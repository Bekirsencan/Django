import django_filters

from .models import Computer


class ComputerFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(field_name='product_name', lookup_expr='contains')
    brand = django_filters.CharFilter(field_name='product_brand', lookup_expr='contains')
    cpu = django_filters.CharFilter(field_name='cpu', lookup_expr='contains')

    class Meta:
        model = Computer
        fields = ['name', 'product_brand', 'cpu', 'operating_system']
