from rest_framework import viewsets

from .models import Category, SubCategory
from .serializers import CategorySerializer, SubCategorySerializer


class CategoryViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None

class SubCategoryViewset(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = None
