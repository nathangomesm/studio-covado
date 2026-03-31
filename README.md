# Studio Côvado | Sistema de Portfólio Dinâmico 🏛️

Um sistema web completo (CMS) desenvolvido com **Python e Django** para gerenciar e exibir o portfólio de um escritório de arquitetura. O foco do projeto é unir um design front-end elegante, com referências editoriais e minimalistas, a um back-end robusto que permite o cadastro dinâmico de novos projetos, categorias e galerias de imagens.

## 🚀 Tecnologias Utilizadas

**Back-end:**
* Python 3
* Django (Arquitetura MVT, ORM, Admin Customizado)
* SQLite (Banco de dados de desenvolvimento)

**Front-end:**
* HTML5 / CSS3 (Design Responsivo, Grid/Flexbox)
* Vanilla JavaScript (Intersection Observer para animações de scroll)
* GLightbox (Galeria de imagens interativa)

## ✨ Principais Funcionalidades

* **Painel Administrativo Customizado:** Interface nativa do Django adaptada para gerenciar projetos, permitindo o upload de múltiplas imagens simultâneas por projeto (relação 1:N).
* **Filtro Dinâmico:** Categorização de projetos (Residencial, Comercial, etc.) no front-end sem necessidade de recarregar a página.
* **Sistema de Galeria Imersiva:** Visualização de projetos em tela cheia com suporte a zoom e navegação mobile-friendly.
* **Efeito Parallax:** Implementação de rolagem imersiva na seção Hero, destacando renders e fotografias arquitetônicas.

## 🛠️ Como executar o projeto localmente

1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/studio-covado.git](https://github.com/SEU-USUARIO/studio-covado.git)

2. Crie e ative o ambiente virtual:
python -m venv venv
* Windows: venv\Scripts\activate
* Linux/Mac: source venv/bin/activate

3. Instale as dependências:
pip install django

4. Execute as migrações do banco de dados:
python manage.py migrate

5. Crie um superusuário para acessar o painel Admin:
python manage.py createsuperuser

6. Inicie o servidor:
python manage.py runserver
Acesse http://127.0.0.1:8000/ no navegador.
