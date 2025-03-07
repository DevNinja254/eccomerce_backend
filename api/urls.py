from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register("products", views.ProductsAPIView, basename="products")
route.register("reviews", views.RevieView, basename="reviews")
route.register("cartegory", views.CartegoryView, basename="cartegory")
route.register("profile", views.ProfileAPIView, basename="profile")
route.register("order", views.OrdeAPIView, basename="order")

urlpatterns = [
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    path('register/', views.UserRegistrationAPIView.as_view(), name='register'),
    path('logout/', views.UserLogoutAPIView.as_view(), name='register'),
    path('token/refresh/', TokenRefreshView.as_view()),
    path("info/", views.UserInfoAPIView.as_view(), name="user-info"),
    path("", include(route.urls))
    
]