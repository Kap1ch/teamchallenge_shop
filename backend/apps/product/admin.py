from django.contrib import admin

from .models import Product, ProductColor, Color, Review

admin.site.register(Product)
admin.site.register(ProductColor)
admin.site.register(Color)
admin.site.register(Review)