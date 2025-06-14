from rest_framework import generics
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, ProductWithReviewsSerializer
from django.db.models import Avg ,Count

class CategoryListView(generics.ListCreateAPIView):  
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveAPIView): 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListView(generics.ListCreateAPIView):  
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):  
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewListView(generics.ListCreateAPIView): 
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(generics.RetrieveAPIView): 
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ProductWithReviewsListView(generics.ListAPIView):
    queryset = Product.objects.annotate(rating=Avg('reviews__stars'))
    serializer_class = ProductWithReviewsSerializer

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.annotate(products_count=Count('products'))
    serializer_class = CategorySerializer
