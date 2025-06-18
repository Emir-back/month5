from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailUpdateDeleteView,
    ProductListCreateView, ProductDetailUpdateDeleteView,
    ReviewListCreateView, ReviewDetailUpdateDeleteView
)

urlpatterns = [
    # Категории
    path('categories/', CategoryListCreateView.as_view()),
    path('categories/<int:pk>/', CategoryDetailUpdateDeleteView.as_view()),

    # Товары
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>/', ProductDetailUpdateDeleteView.as_view()),

    # Отзывы
    path('reviews/', ReviewListCreateView.as_view()),
    path('reviews/<int:pk>/', ReviewDetailUpdateDeleteView.as_view()),
]
