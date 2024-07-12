from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from rest_framework.permissions import AllowAny
from users.api.serializers import UserSerializer, UserListSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Define the schema for User GET and POST requests
@swagger_auto_schema(
    method='get',
    operation_description="Obtener lista de todos los usuarios.",
    operation_summary="Obtener lista de los usuarios",
    responses={200: UserListSerializer(many=True)},
    tags=['Usuarios']
)
@swagger_auto_schema(
    method='post',
    operation_description="Crea un nuevo usuario",
    operation_summary="Crea un usuario",
    request_body=UserSerializer,
    responses={201: UserSerializer},
    tags=['Usuarios']
)
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def user_api_view(request):
    """
    Handle GET and POST requests for User.
    """
    # Handle GET request to list all users
    if request.method == 'GET':
        # Retrieve all users with specific fields
        users = User.objects.all().values('id', 'username', 'email', 'password')
        # Serialize the queryset
        users_serializers = UserListSerializer(users, many=True)
        # Return serialized data with HTTP 200 OK
        return Response(users_serializers.data, status=status.HTTP_200_OK)

    # Handle POST request to create a new user
    elif request.method == 'POST':
        # Deserialize the incoming data
        user_serializer = UserSerializer(data=request.data)
        
        # Check if data is valid
        if user_serializer.is_valid():
            # Save the user
            user_serializer.save()
            # Return serialized data with HTTP 201 Created
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        # Return errors if data is invalid
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Define the schema for User Detail GET, PUT, and DELETE requests
@swagger_auto_schema(
    method='get',
    operation_description="Obtener detalles del usuario por ID.",
    operation_summary="Obtener información del usuario por ID",
    responses={200: UserSerializer},
    tags=['Usuarios']
)
@swagger_auto_schema(
    method='put',
    operation_description="Actualiza los datos de un usuario por ID.",
    operation_summary="Actualiza un usuario",
    request_body=UserSerializer,
    responses={200: UserSerializer},
    tags=['Usuarios']
)
@swagger_auto_schema(
    method='delete',
    operation_description="Elimina un usario por ID.",
    operation_summary="Eliminar usuario",
    responses={200: openapi.Response(description="Usuario eliminado")},
    tags=['Usuarios']
)
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def user_detail_api_view(request, pk=None):
    """
    Handle GET, PUT, and DELETE requests for a specific User.
    """
    # Retrieve the user by primary key
    user = User.objects.filter(id=pk).first()

    # Check if user exists
    if user:
        # Handle GET request to retrieve user details
        if request.method == 'GET':
            # Serialize the user
            user_serializer = UserSerializer(user)
            # Return serialized data with HTTP 200 OK
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        # Handle PUT request to update user details
        elif request.method == 'PUT':
            # Deserialize and update the user
            user_serializer = UserSerializer(user, data=request.data)
            # Check if data is valid
            if user_serializer.is_valid():
                # Save the updated user
                user_serializer.save()
                # Return serialized data with HTTP 200 OK
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            # Return errors if data is invalid
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Handle DELETE request to delete user
        elif request.method == 'DELETE':
            # Delete the user
            user.delete()
            # Return success message with HTTP 200 OK
            return Response({'message': 'Usuario eliminado'}, status=status.HTTP_200_OK)
    
    # Return error message if user does not exist
    return Response({'message': 'No se ha encontrado un usuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

# Define the schema for getting user info by email
@swagger_auto_schema(
    method='post',
    operation_description="Obtener información por email.",
    operation_summary="Obtener usuario por email",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email del usuario')
        }
    ),
    responses={200: openapi.Response(
        description="User ID",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Id del usuario')
            }
        )
    )},
    tags=['Usuarios']
)
@api_view(['POST'])
@permission_classes([AllowAny])
def get_user_info_by_email(request):
    """
    Handle POST request to get user info by email.
    """
    # Get email from request data
    email = request.data.get('email')

    # Retrieve the user by email
    user = User.objects.filter(email=email).first()
    if not user:
        # Return error message if user does not exist
        return Response({'error': 'No se encontró ningún usuario con este correo electrónico'}, status=status.HTTP_400_BAD_REQUEST)

    # Prepare user data to return
    user_data = {
        'id': user.id
    }
    # Return user data with HTTP 200 OK
    return Response(user_data, status=status.HTTP_200_OK)
