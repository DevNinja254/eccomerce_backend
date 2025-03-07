from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from products.models import Product, Cartegory, Review
from products.serializer import *
from users.serializers import *
from .pagination import CustomPagination
from .filter import *
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from users.models import Profile
from datetime import date 

class UserRegistrationAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data['tokens'] = {
            "refresh": str(token),
            'access': str(token.access_token)
        }
        return Response(data, status=status.HTTP_201_CREATED)
class UserLoginAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        serializer = UserSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data['tokens'] = {
            "refresh": str(token),
            'access': str(token.access_token)
        }
        return Response(data, status=status.HTTP_200_OK)

class UserLogoutAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try: 
            refresh_token = request.data
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserInfoAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user
class ProfileAPIView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'user'
    
class ProductsAPIView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (AllowAny,)
    # http_method_names = ['get', 'head', 'option']
    pagination_class = CustomPagination
    filterset_class = ProductFilter

class OrdeAPIView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (AllowAny,)
    filterset_class = OrderFilter
    

class RevieView(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
class CartegoryView(viewsets.ModelViewSet):
    serializer_class = CartegorySerializer
    queryset = Cartegory.objects.all()

