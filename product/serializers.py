from rest_framework import serializers
from .models import Category, Product, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars', 'product']  
    def validate_text(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Отзыв слишком короткий.")
        return value

    def validate_stars(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Оценка должна быть от 1 до 5.")
        return value
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название не может быть пустым.")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Цена не может быть отрицательной.")
        return value

    def validate_description(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Описание должно быть не менее 5 символов.")
        return value

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название не может быть пустым.")
        if len(value) < 2:
            raise serializers.ValidationError("Название слишком короткое.")
        return value


class ProductWithReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'reviews', 'rating']
