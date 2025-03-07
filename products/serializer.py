from rest_framework import serializers
from .models import *

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
class CartegorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cartegory
        fields = "__all__"
class ProductSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many = True, read_only=True)
    class Meta:
        model = Product
        fields = "__all__"
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"