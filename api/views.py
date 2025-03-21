from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from products.models import *
from products.serializer import *
from users.serializers import *
from .pagination import *
from .filter import *
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from users.models import Profile
from datetime import date, timedelta 
from django.utils import timezone
import logging, base64, json, requests
from users.models import PaymentWaiting
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
logger = logging.getLogger(__name__)
class UserLogoutAPIView(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        logger.debug(request.data)
        try: 
            refresh_token = request.data
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Logout Error: {e}")
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

class SearchAPIView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'head', 'option']
    filter_backends = [SearchFilter]
    search_fields = ['title']
    pagination_class = None

class OrdeAPIView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (AllowAny,)
    filterset_class = OrderFilter
    pagination_class = None
    

class RevieView(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
class CartegoryView(viewsets.ModelViewSet):
    serializer_class = CartegorySerializer
    queryset = Cartegory.objects.all()
    http_method_names = ['get', 'head', 'option']
    filter_backends = [SearchFilter]
    search_fields = ['cartegory_name']
    pagination_class = None   
class CartegoryGroupView(viewsets.ModelViewSet):
    serializer_class = CartegoryGroupSerializer
    queryset = CartegoryGroup.objects.all()
    http_method_names = ['get', 'head', 'option']
    pagination_class = None

class CartAPIView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    filterset_class = CartFilter
    pagination_class = None
@api_view(['POST'])
def payment(request):
        if request.method == "POST":
            username = request.data["username"]
            Amount = int(request.data["amount"])
            number = str(request.data["phone_number"])
            phoneNumber = "254" + number[1:]
            # Your API username and password
            api_username = "7v1lCadGn6V2AstOB8LD"
            api_password = "CHKjuI9dQdRWgMXAof7ip4rMIkopntZrT3G0zgRc"
            # Concatenating username and password with colon
            credentials = f'{api_username}:{api_password}'
            # Base64 encode the credentials
            encoded_credentials = base64.b64encode(credentials.encode()).decode()
            # Creating the Basic Auth token
            basic_auth_token = f'Basic {encoded_credentials}'
            # Output the token
            # print(basic_auth_token)
            url = 'https://backend.payhero.co.ke/api/v2/payments'
            headers = {
                'Content-Type': 'application/json',
                'Authorization': basic_auth_token
            }
            logger.info("sending data")
            data = {
                "amount": Amount,
                "phone_number": phoneNumber,
                "channel_id": 1786,
                "provider": "m-pesa",
                "external_reference": "INV-009",
                "callback_url":"https://smooth-vast-thrush.ngrok-free.app/processPayment/"
            }
            response = requests.post(url, json=data, headers=headers).json()
            if response["success"]:
                PaymentWaiting.objects.get_or_create(
                    username = username,
                    amount = Amount,
                    phone_number = phoneNumber
                )
            return Response(response, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
