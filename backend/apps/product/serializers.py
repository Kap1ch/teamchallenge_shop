from django.db.models import Avg
from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField

from apps.catalog.models import SubCategory
from .models import Product, Review, ProductColor, Material


class ReviewSerializer(ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'rating', 'review_text', 'user', 'created']

    def get_user(self, obj):
        first_name = obj.user.first_name or ''
        last_name = obj.user.last_name or ''
        if first_name:
            return f"{last_name} {first_name[0]}."
        return last_name


class ProductColorSerializer(ModelSerializer):
    color_name = CharField(source='color.name', read_only=True)
    hex = CharField(source='color.color', read_only=True)

    class Meta:
        model = ProductColor
        fields = ['id', 'image_url', 'is_main', 'color_name', 'hex']


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name']


class MaterialSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name', 'created', ]


class ProductDetailSerializer(ModelSerializer):
    subcategory = SubCategorySerializer(read_only=True)
    material = MaterialSerializer(read_only=True)
    reviews = SerializerMethodField()
    productcolors = ProductColorSerializer(many=True, read_only=True)
    avg_rating = SerializerMethodField()
    # size = ReadOnlyField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'depth', 'width', 'height', 'slug',
            'price', 'stock', 'subcategory', 'material', 'avg_rating',
            'reviews', 'productcolors', 'created',
        ]

    def get_reviews(self, obj):
        reviews = obj.reviews.all().order_by('-created')[:5]
        return ReviewSerializer(reviews, many=True).data

    def get_avg_rating(self, obj):
        return round(obj.reviews.aggregate(avg=Avg('rating'))['avg'] or 0, 2)
