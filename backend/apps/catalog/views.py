from rest_framework import viewsets

from .models import Catalog, SubCategory
from .serializers import CatalogSerializer, SubCategorySerializer


class CatalogViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

class SubCategoryViewset(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer