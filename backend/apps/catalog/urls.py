from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewset, SubCategoryViewset

router = DefaultRouter()
router.register(r'category', CategoryViewset, basename='catalog')
router.register(r'subcategory', SubCategoryViewset, basename='subcategory')

app_name = 'catalog_api'
urlpatterns = [
    path('', include(router.urls)),
]
