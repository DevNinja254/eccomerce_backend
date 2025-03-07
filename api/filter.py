import django_filters 
from products.models import Product, Order

class ProductFilter(django_filters.FilterSet):
    cartegory = django_filters.CharFilter(field_name='cartegory', lookup_expr='exact')
    exclusive = django_filters.BooleanFilter(field_name='exclusive', lookup_expr='exact')
    offer = django_filters.BooleanFilter(field_name='offer', lookup_expr='exact')
    trending = django_filters.BooleanFilter(field_name='trending', lookup_expr='exact')
    pk= django_filters.CharFilter(field_name='title', lookup_expr='exact', label="pk")
    general= django_filters.CharFilter(field_name='title', lookup_expr='contains', label="general")
    class Meta:
        model = Product
        fields = ['cartegory', "exclusive", "offer", "trending", "title"]

class OrderFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='username', lookup_expr='exact')
    
    class Meta:
        model = Order
        fields = ['username']  