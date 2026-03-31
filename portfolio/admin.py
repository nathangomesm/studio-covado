from django.contrib import admin
from .models import Categoria, Projeto, ImagemProjeto # <-- Importe o novo model

# Configuração para as imagens aparecerem dentro do Projeto
class ImagemInline(admin.TabularInline):
    model = ImagemProjeto
    extra = 1 # Quantos campos vazios aparecem por padrão

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'ativo', 'data_publicacao')
    list_filter = ('categoria', 'ativo')
    search_fields = ('titulo', 'descricao')
    
    # Essa linha mágica conecta a galeria ao projeto
    inlines = [ImagemInline]