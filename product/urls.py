from django.urls import path
from .views import (
    CategoryListView, CategoryDetailView,
    ProductListView, ProductDetailView,
    ReviewListView, ReviewDetailView,
    ProductWithReviewsListView
)

urlpatterns = [
    # Категории
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),

    # Продукты
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    
    # Продукты с отзывами и рейтингом
    path('products/reviews/', ProductWithReviewsListView.as_view()),

    # Отзывы
    path('reviews/', ReviewListView.as_view()),
    path('reviews/<int:pk>/', ReviewDetailView.as_view()),
]
