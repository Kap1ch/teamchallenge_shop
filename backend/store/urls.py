from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from apps.catalog.views import CatalogViewset

schema_view = get_swagger_view(title='HVOYA API')
router = DefaultRouter()
router.register(r'catalog', CatalogViewset, basename='catalog')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view),
]

urlpatterns += router.urls
