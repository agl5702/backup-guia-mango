from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
from users.api.serializers import CustomTokenObtainPairSerializer,CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class Login(TokenObtainPairView):
    serializer_class= CustomTokenObtainPairSerializer

    def post(self,request,*args,**kwargs):
        username= request.data.get('username','')
        password = request.data.get('password','')
        user = authenticate(
            username=username,
            password=password)
        if user:
            login_serializer= self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response ({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token':login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message':'Inicio de Sesion Exitoso'
                },status=status.HTTP_200_OK)
            return Response({
                'error': 'Nombre o contraseña incorrectos'
            },status=status.HTTP_400_BAD_REQUEST)
        return Response({
                'error': 'Nombre o contraseña incorrectos'
            },status=status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):
    permission_classes = (IsAuthenticated,) 

    def post(self, request, *args, **kwargs):
        # Obtener el usuario autenticado desde la solicitud
        user = request.user

        # Invalidar todos los tokens de actualización asociados con el usuario
        RefreshToken.for_user(user)

        return Response({
            'message': 'Sesión cerrada correctamente.'
        }, status=status.HTTP_200_OK)