from rest_framework import generics
from .models import Product
from .serializers import ProductDetailSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all().prefetch_related(
        'reviews__user',
        'productcolors__color',
    ).select_related('subcategory', 'material')
    serializer_class = ProductDetailSerializer
