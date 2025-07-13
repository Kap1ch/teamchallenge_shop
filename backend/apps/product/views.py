from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .models import Product
from .serializers import ProductDetailSerializer, ProductAllSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all().prefetch_related(
        'reviews__user',
        'productcolors__color',
    ).select_related('subcategory')
    serializer_class = ProductDetailSerializer


class ProductAllView(generics.ListAPIView):
    serializer_class = ProductAllSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        subcategory_id = self.kwargs.get('subcategory_id')

        if category_id:
            queryset = Product.objects.filter(subcategory__category__id=category_id)
        elif subcategory_id:
            queryset = Product.objects.filter(subcategory__id=subcategory_id)
        else:
            queryset = Product.objects.all()

        return queryset


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)
