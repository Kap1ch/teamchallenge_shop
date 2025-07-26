from django_filters import rest_framework as filters
from .models import Product

from apps.core.filters import CharInFilter



class ProductFilter(filters.FilterSet):
    subcategory = filters.CharFilter(field_name='subcategory__slug', lookup_expr='iexact')
    color = CharInFilter(field_name='productcolors__color__name', lookup_expr='in')
    material = CharInFilter(field_name='materials__name', lookup_expr='in')
    price = filters.RangeFilter()
    class Meta:
        model = Product
        fields = ['subcategory', 'color', 'material', 'price']
