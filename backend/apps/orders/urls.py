from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')


app_name = 'orders_api'
urlpatterns = [
    path('', include(router.urls)),
]
