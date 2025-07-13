from django.urls import path

from .views import ProductDetailView, ProductAllView

app_name = 'product_api'
urlpatterns = [
    path('', ProductAllView.as_view(), name='all-products'),
    path('category/<uuid:category_id>/', ProductAllView.as_view(), name='all-category-products'),
    path('subcategory/<uuid:subcategory_id>/', ProductAllView.as_view(), name='all-subcategory-products'),
    path('<uuid:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
