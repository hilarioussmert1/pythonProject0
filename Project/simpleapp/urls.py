from django.urls import path
from .views import ProductsList, ProductDetail, create_products

urlpatterns = [
    path('', ProductsList.as_view()),
    path('<int:pk>', ProductDetail.as_view()),
    path('create/', create_products, name='product_create')
]
