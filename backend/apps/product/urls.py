from django.urls import path

from .views import ProductDetailView

app_name = 'product_api'
urlpatterns = [
    path('<uuid:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
