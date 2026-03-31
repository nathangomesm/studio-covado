# Adicione get_object_or_404 nas importações
from django.shortcuts import render, get_object_or_404
from .models import Projeto, Categoria

def home(request):
    # ... (seu código da home continua igual) ...
    projetos = Projeto.objects.filter(ativo=True)
    categorias = Categoria.objects.all()
    contexto = {'projetos': projetos, 'categorias': categorias}
    return render(request, 'portfolio/home.html', contexto)

# --- Nova Função ---
def detalhe_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    
    # NÃO PRECISAMOS MAIS DA GALERIA FAKE
    # O Django já traz as imagens reais automaticamente pelo 'related_name'
    
    contexto = {
        'projeto': projeto
        # Removemos a chave 'galeria' daqui, pois acessaremos direto no HTML via projeto.imagens.all
    }
    return render(request, 'portfolio/projeto_detalhe.html', contexto)