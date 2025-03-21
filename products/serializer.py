from rest_framework import serializers
from .models import *

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    cartegory = serializers.StringRelatedField()
    review = ReviewSerializer(many = True, read_only=True)
    class Meta:
        model = Product
        fields = "__all__"

class CartegorySerializer(serializers.ModelSerializer):
    product_cartegory = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Cartegory
        fields = "__all__"
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class CartegoryGroupSerializer(serializers.ModelSerializer):
    cartegory_group = CartegorySerializer(many=True, read_only=True)
    class Meta:
        model = CartegoryGroup
        fields = "__all__"
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"