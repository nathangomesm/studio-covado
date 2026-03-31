from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Nova rota para detalhes:
    # <int:id> é a "variável" que pega o número do projeto na URL
    path('projeto/<int:id>/', views.detalhe_projeto, name='detalhe_projeto'),
]