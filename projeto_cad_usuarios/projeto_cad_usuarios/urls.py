

from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    # usuarios.com
    path('',views.home,name='home'),
    #usuarios.com/usuarios
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('excluir/<int:id>/', views.excluir_usuario, name='excluir_usuario')
    
]
