from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CatalogViewset

router = DefaultRouter()
router.register(r'catalog', CatalogViewset, basename='catalog')

app_name = 'catalog_api'
urlpatterns = [
    path('', include(router.urls)),
]
