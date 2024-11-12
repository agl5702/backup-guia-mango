import pytest
from users.models import User

# Prueba para la creacion de un usuario común.	
@pytest.mark.django_db
def test_user_creation():



    user=User.objects.create_user(
        username='angel',
        email='angel@example.com',
        name='angel',
        last_name='vasquez',
        password='test123',
        is_staff= False

    )
    assert user.username == 'angel'

# Prueba para la creacion de un usuario administrador.	

@pytest.mark.django_db
def test_superuser_creation():



    user=User.objects.create_superuser(
        username='angel',
        email='angel@example.com',
        name='angel',
        last_name='vasquez',
        password='test123'
    )
    assert user.username == 'angel'


# Prueba para la verificacion si un usuario es staff.	
@pytest.mark.django_db
def test_staff_user_creation():



    user=User.objects.create_superuser(
        username='angel',
        email='angel@example.com',
        name='angel',
        last_name='vasquez',
        password='test123'
    )
    assert user.is_staff


