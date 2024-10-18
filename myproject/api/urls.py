from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet

# Criando o router e registrando o ViewSet de Author
router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='authors')

# Definindo as rotas de autenticação e as rotas do router
urlpatterns = [
    # Rotas para obtenção e atualização de tokens JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Incluindo as rotas do ViewSet de autores geradas pelo router
    path('', include(router.urls)),
]
