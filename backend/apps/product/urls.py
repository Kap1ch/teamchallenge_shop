from django.urls import path

from .views import ProductDetailView, ProductAllView, ProductFilterOptionsView, NewArrivalProductView, product_filter_opt

app_name = 'product_api'
urlpatterns = [
    path('', ProductAllView.as_view(), name='all-products'),
    path('new_arrival/', NewArrivalProductView.as_view(), name='new_arrival-product'),
    path('category/<uuid:category_id>/', ProductAllView.as_view(), name='all-category-products'),
    path('subcategory/<uuid:subcategory_id>/', ProductAllView.as_view(), name='all-subcategory-products'),
    # path('filters/', ProductFilterOptionsView.as_view(), name='product-filter-options'),
    path('filters/', product_filter_opt, name='product-filter-options'),
    path('<str:slug>/', ProductDetailView.as_view(), name='product-detail'),

]
