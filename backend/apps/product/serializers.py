from django.db.models import Avg
from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField

from apps.catalog.models import Category, SubCategory
from .models import Product, Review, ProductColor


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
        fields = ['id', 'name', 'slug', 'image_url']
        ref_name = 'ProductSubCategory'


class ProductDetailSerializer(ModelSerializer):
    subcategory = SubCategorySerializer(read_only=True)
    reviews = SerializerMethodField()
    productcolors = ProductColorSerializer(many=True, read_only=True)
    avg_rating = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'material', 'depth', 'width', 'height', 'slug',
            'price', 'stock', 'subcategory', 'avg_rating',
            'reviews', 'productcolors', 'created',
        ]

    def get_reviews(self, obj):
        reviews = obj.reviews.all().order_by('-created')

        return {
            'count': reviews.count(),
            'items': ReviewSerializer(reviews[:5], many=True).data}


    def get_avg_rating(self, obj):
        return round(obj.reviews.aggregate(avg=Avg('rating'))['avg'] or 0, 2)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image_url', 'slug']
        ref_name = 'AllProductCategory'


class SubCatAllProductSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'category', 'name', 'slug', 'image_url']


class ProductAllSerializer(ModelSerializer):
    subcategory = SubCatAllProductSerializer(read_only=True)
    image = SerializerMethodField(read_only=True)
    avg_rating = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'slug',
                  'price', 'stock', 'subcategory', 'avg_rating', 'image',
                  'created']

    def get_image(self, obj):
        image = obj.productcolors.filter(is_main=True).order_by('-created').first()
        if image:
            return image.image_url.url

    def get_avg_rating(self, obj):
        return round(obj.reviews.aggregate(avg=Avg('rating'))['avg'] or 0, 2)


# class ProductFilterOptionsSerializer(ModelSerializer):
#     class Meta:
#         model =