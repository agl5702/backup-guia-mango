from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from rest_framework.permissions import AllowAny
from users.api.serializers import UserSerializer,UserListSerializer
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes


@api_view(['GET','POST'])
@permission_classes([AllowAny])
def user_api_view(request):

    # list
    if request.method == 'GET':
        # queryset
        users= User.objects.all().values('id','username','email','password')
        users_serializers= UserListSerializer(users, many=True)
        return Response(users_serializers.data,status=status.HTTP_200_OK)

    #create
    elif request.method == 'POST':
        user_serializer= UserSerializer(data = request.data)
        
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data,status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors)
    



#View detail 
@api_view(['GET','PUT','DELETE'])
@permission_classes([AllowAny])

def user_detail_api_view(request,pk=None):#The 'pk' is the parameter to filter

    # queryset
    user = User.objects.filter(id= pk).first() # Optimized

    # Validation
    if user:
        # retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response (user_serializer.data,status=status.HTTP_200_OK)
        
        # update
        if request.method == 'PUT':
            user_serializer= UserSerializer(user,data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response (user_serializer.data,status=status.HTTP_200_OK)
            return Response (user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # delete
        if request.method == 'DELETE':
            user.delete()
            return Response({'message':'Usuario eliminado'}, status=status.HTTP_200_OK)
        
    return Response({'message': 'No se ha encontrado un usario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def get_user_info_by_email(request):
    email = request.data.get('email')

    # Verifica si el correo electrónico es válido y está asociado a un usuario registrado
    user = User.objects.filter(email=email).first()
    if not user:
        return Response({'error': 'No se encontró ningún usuario con este correo electrónico'}, status=400)

    user_data={
        'id': user.id
    }
    # Obtiene la información del usuario y la devuelve como respuesta
    return Response(user_data, status=200)