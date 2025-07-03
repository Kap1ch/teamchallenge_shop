from django.contrib import admin

from .models import Product, ProductImage, Color, Review

admin.register(Product)
admin.register(ProductImage)
admin.register(Color)
admin.register(Review)