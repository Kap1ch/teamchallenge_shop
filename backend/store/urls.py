from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="HVOYA API",
      default_version='v1',
      description="Документація API для HVOYA",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/catalog/', include('apps.catalog.urls', namespace='catalog_api')),
    path('api/products/', include('apps.product.urls', namespace='product_api')),
    path('api/auth/', include('apps.account.urls', namespace='auth')),


]

