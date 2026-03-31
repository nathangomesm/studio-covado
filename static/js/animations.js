document.addEventListener("DOMContentLoaded", function () {
    // Seleciona todos os elementos que queremos animar
    const elementsToAnimate = document.querySelectorAll('.fade-in-section');

    // Configura o observador
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            // Se o elemento entrou na tela
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
            }
        });
    }, {
        threshold: 0.1 // Dispara quando 10% do elemento estiver visível
    });

    // Manda observar cada elemento
    elementsToAnimate.forEach(element => {
        observer.observe(element);
    });

    // Animação especial para o Hero carregar assim que abrir a página
    setTimeout(() => {
        const heroText = document.querySelector('.frase-efeito');
        if (heroText) {
            heroText.style.opacity = '1';
            heroText.style.transform = 'translateY(0)';
            heroText.style.transition = 'all 1s ease';
        }
    }, 200);
});

// ... (seu código do Observer/Scroll continua aqui em cima) ...

// Função de Filtragem
function filtrarProjetos(categoriaId, botaoClicado) {
    // 1. Remove a classe 'ativo' de todos os botões
    const botoes = document.querySelectorAll('.btn-filtro');
    botoes.forEach(btn => btn.classList.remove('ativo'));

    // 2. Adiciona 'ativo' apenas no botão clicado
    botaoClicado.classList.add('ativo');

    // 3. Pega todos os projetos
    const projetos = document.querySelectorAll('.card-projeto');

    // 4. Mostra ou Esconde
    projetos.forEach(projeto => {
        const catProjeto = projeto.getAttribute('data-categoria');

        if (categoriaId === 'todos' || catProjeto === categoriaId) {
            projeto.style.display = 'block';
            // Pequeno timeout para permitir animação (opcional)
            setTimeout(() => projeto.style.opacity = '1', 50);
        } else {
            projeto.style.display = 'none';
            projeto.style.opacity = '0';
        }
    });
}

// Menu Mobile
function toggleMenu() {
    const nav = document.querySelector('.nav-links');
    const hamburger = document.querySelector('.hamburger');
    
    nav.classList.toggle('active');
    hamburger.classList.toggle('active');
}