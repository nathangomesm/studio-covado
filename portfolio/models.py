from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    # Ex: Comercial, Corporativo, Residencial, Institucional

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='projetos')
    imagem_principal = models.ImageField(upload_to='projetos/')
    data_publicacao = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    
    # --- NOVOS CAMPOS: FICHA TÉCNICA ---
    cliente = models.CharField(max_length=100, default="Confidencial")
    localizacao = models.CharField(max_length=200, default="A definir", help_text="Ex: Lages, SC")
    area = models.CharField(max_length=50, default="A definir", help_text="Ex: 450m²")
    status = models.CharField(max_length=100, default="Concluído")

    def __str__(self):
        return self.titulo

class ImagemProjeto(models.Model):
    # O 'related_name' é o segredo. Ele permite acessar as imagens pelo projeto (projeto.imagens.all)
    projeto = models.ForeignKey(Projeto, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='projetos/galeria/')

    def __str__(self):
        return f"Imagem de {self.projeto.titulo}"