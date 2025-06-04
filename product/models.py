from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
