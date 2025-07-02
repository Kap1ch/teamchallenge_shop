from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Catalog, SubCategory


class CatalogSerializer(ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'


class SubCategorySerializer(ModelSerializer):
    category = CatalogSerializer(read_only=True)
    category_id = PrimaryKeyRelatedField(
        queryset=Catalog.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = SubCategory
        fields = '__all__'
