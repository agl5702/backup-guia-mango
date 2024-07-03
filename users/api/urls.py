from django.urls import path
from users.api.api import user_api_view, user_detail_api_view,get_user_info_by_email

urlpatterns = [
    path('usuario/', user_api_view, name='usuario_api'),
    path('usuario/<int:pk>/',user_detail_api_view, name='user_detail_api_view'),
    path('verificar-usuario/',get_user_info_by_email, name='verify_user_email'),
]
