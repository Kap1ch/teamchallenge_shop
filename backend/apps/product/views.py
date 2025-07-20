from rest_framework import generics, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Min, Max

from apps.catalog.models import Category, SubCategory

from .models import Product, Color, ProductColor
from .serializers import ProductDetailSerializer, ProductAllSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all().prefetch_related(
        'reviews__user',
        'productcolors__color',
    ).select_related('subcategory')
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'



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
        return Response(serializer.data)


class NewArrivalProductView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-created')[:8]
    serializer_class = ProductAllSerializer
    pagination_class = None



class ProductFilterOptionsView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()

        subcategories = SubCategory.objects.filter(
            id__in=products.values_list('subcategory_id', flat=True).distinct()
        ).values('id', 'name', 'slug')

        categories = Category.objects.filter(id__in=products.values_list('subcategory__category', flat=True).distinct()
                                             ).values('id', 'name', 'slug')

        colors = Color.objects.filter(
            id__in=ProductColor.objects.values_list('color_id', flat=True).distinct()
        ).values('id', 'name', 'color')

        price_range = products.aggregate(
            price_min=Min('price'),
            price_max=Max('price')
        )

        return Response({
            'categories': list(categories),
            'subcategories': list(subcategories),
            'colors': list(colors),
            'price_min': price_range['price_min'],
            'price_max': price_range['price_max'],
        }, status=status.HTTP_200_OK)
