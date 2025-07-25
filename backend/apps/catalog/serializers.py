from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Category, SubCategory


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        ref_name = 'CatalogCategory'


class SubCategorySerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = SubCategory
        fields = '__all__'
        ref_name = 'CatalogSubCategory'
