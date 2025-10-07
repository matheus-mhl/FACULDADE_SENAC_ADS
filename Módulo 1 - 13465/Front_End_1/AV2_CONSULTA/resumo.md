<!-- =======================================================
✅ RESUMO COMPLETO: BOOTSTRAP
======================================================= -->

<!-- ====================================
📌 O QUE É O BOOTSTRAP?
==================================== -->
<!--
Bootstrap é um framework front-end que facilita a criação de sites responsivos e modernos.

Ele fornece:
✔️ Um sistema de grid (grade) para criar layouts flexíveis.
✔️ Componentes prontos (botões, cards, navegação, alertas, etc).
✔️ Classes utilitárias para espaçamentos, cores, tamanhos, alinhamentos, etc.
✔️ Funcionalidades com JavaScript (modal, carrossel, menu colapsável, etc).
-->

<!-- ====================================
🚀 COMO USAR O BOOTSTRAP EM UM PROJETO
==================================== -->

<!--
1. Incluir o Bootstrap via CDN (forma mais simples)
-->

<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Exemplo com Bootstrap</title>

  <!-- CSS do Bootstrap -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

  <!-- JS do Bootstrap (opcional, para componentes interativos como modais) -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>
  <!-- Conteúdo aqui -->
</body>
</html>

<!--
2. Ou, você pode instalar via npm ou baixar os arquivos, se estiver usando projetos locais mais avançados.
-->

<!-- ====================================
🔲 SISTEMA DE GRID (GRADE)
==================================== -->

<!--
O Bootstrap divide a tela em 12 colunas.
Você usa classes para organizar os elementos em colunas e linhas.
-->

<!-- EXEMPLO DE GRID RESPONSIVO -->
<div class="container">
  <div class="row">
    <div class="col-12 col-md-6 col-lg-4">
      <!-- Ocupa toda a linha em telas pequenas, metade em médias, 1/3 em grandes -->
      <p>Coluna Responsiva</p>
    </div>
    <div class="col-12 col-md-6 col-lg-8">
      <p>Outra Coluna Responsiva</p>
    </div>
  </div>
</div>

<!-- Classes principais:
- container: cria margem automática
- row: define uma linha
- col, col-*, col-md-*, col-lg-* : define colunas e tamanhos
-->

<!-- ====================================
🎨 CORES E UTILITÁRIOS DE ESTILO
==================================== -->

<!-- Texto -->
<p class="text-primary">Texto azul (primário)</p>
<p class="text-danger">Texto vermelho (perigo)</p>

<!-- Fundo -->
<div class="bg-success text-white p-3">Fundo verde com texto branco</div>

<!-- Espaçamento -->
<div class="mt-3 mb-2 p-4">Margem superior 3, inferior 2, padding 4</div>

<!-- Alinhamento -->
<p class="text-center">Centralizado</p>
<p class="text-end">Alinhado à direita</p>

<!-- Bordas e sombreamento -->
<div class="border rounded shadow p-3">Com borda, canto arredondado e sombra</div>

<!--
Classes como:
- m (margin), p (padding)
- text-*, bg-*, border
- rounded, shadow, etc
-->

<!-- ====================================
🔘 COMPONENTES PRONTOS
==================================== -->

<!-- Botão -->
<button class="btn btn-primary">Clique Aqui</button>

<!-- Alerta -->
<div class="alert alert-warning" role="alert">
  Este é um alerta de aviso!
</div>

<!-- Card -->
<div class="card" style="width: 18rem;">
  <img src="https://via.placeholder.com/150" class="card-img-top" alt="Imagem">
  <div class="card-body">
    <h5 class="card-title">Título do Card</h5>
    <p class="card-text">Descrição do conteúdo do card.</p>
    <a href="#" class="btn btn-success">Ação</a>
  </div>
</div>

<!-- Barra de navegação (Navbar) -->
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Logo</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menu">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="menu">
      <ul class="navbar-nav me-auto">
        <li class="nav-item"><a class="nav-link active" href="#">Início</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Sobre</a></li>
      </ul>
    </div>
  </div>
</nav>

<!-- Modal -->
<button type="button" class="btn btn-info" data-bs-toggle="modal" data-bs-target="#meuModal">
  Abrir Modal
</button>

<div class="modal fade" id="meuModal" tabindex="-1">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Título do Modal</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body">
        Conteúdo do modal aqui.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button>
      </div>
    </div>
  </div>
</div>

<!--
Todos os componentes estão documentados aqui:
https://getbootstrap.com/docs/5.3/components/alerts/
-->

<!-- ====================================
📱 DESIGN RESPONSIVO
==================================== -->

<!--
O Bootstrap funciona por *breakpoints* que ajustam o layout em diferentes tamanhos de tela:

- Extra pequeno (xs): <576px
- Pequeno (sm): ≥576px
- Médio (md): ≥768px
- Grande (lg): ≥992px
- Extra grande (xl): ≥1200px

Exemplo:
- col-12: ocupa 100% em qualquer tamanho
- col-md-6: ocupa 50% a partir de md (768px)
- col-lg-4: ocupa 1/3 a partir de lg (992px)
-->

<!-- ====================================
✅ DICAS ÚTEIS
==================================== -->

<!--
✔️ Use sempre <div class="container"> para centralizar o conteúdo.
✔️ Use a documentação oficial como referência: https://getbootstrap.com/docs
✔️ Teste o comportamento redimensionando a janela ou usando o inspetor do navegador (modo mobile).
✔️ Combine classes Bootstrap com seu próprio CSS, se necessário.
✔️ Use a versão mais atual do Bootstrap (no momento: 5.3.3)
-->

<!--Dica extra:-->
<!--Shif + alt + F para identar codigo-->
