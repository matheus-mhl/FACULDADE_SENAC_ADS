<!--
RESUMO DETALHADO DO SISTEMA DE GRID DO BOOTSTRAP 5
--------------------------------------------------
O Bootstrap utiliza um sistema de 12 colunas para criar layouts responsivos e flexíveis.
O sistema é baseado em containers, rows (linhas) e columns (colunas).

1. Container:
    - Serve como um contêiner para todo o conteúdo.
    - Pode ser .container (fixo) ou .container-fluid (100% da largura).

2. Row:
    - Representa uma linha dentro do container.
    - Deve envolver colunas.

3. Column:
    - Divide a largura da linha em 12 partes.
    - Exemplo: col-6 ocupa metade da linha (6/12).
    - Pode ser responsivo: col-sm-6, col-md-4, etc.
-->

<div class="container">
  <!-- EXEMPLO 1: Linha com 2 colunas iguais -->
  <div class="row">
    <div class="col-6 bg-primary text-white">Coluna 1 (6/12)</div>
    <div class="col-6 bg-secondary text-white">Coluna 2 (6/12)</div>
  </div>

  <!-- EXEMPLO 2: Três colunas de 4 partes -->
  <div class="row mt-3">
    <div class="col-4 bg-success text-white">Coluna 1 (4/12)</div>
    <div class="col-4 bg-warning text-dark">Coluna 2 (4/12)</div>
    <div class="col-4 bg-danger text-white">Coluna 3 (4/12)</div>
  </div>

  <!-- EXEMPLO 3: Colunas com tamanhos diferentes -->
  <div class="row mt-3">
    <div class="col-3 bg-info text-white">Coluna 1 (3/12)</div>
    <div class="col-9 bg-dark text-white">Coluna 2 (9/12)</div>
  </div>

  <!-- EXEMPLO 4: Colunas responsivas -->
  <div class="row mt-3">
    <div class="col-12 col-md-6 bg-light text-dark">Coluna 1 (100% em telas pequenas, 50% em md+)</div>
    <div class="col-12 col-md-6 bg-secondary text-white">Coluna 2 (100% em telas pequenas, 50% em md+)</div>
  </div>

  <!-- EXEMPLO 5: Colunas automáticas com "col" -->
  <div class="row mt-3">
    <div class="col bg-primary text-white">Auto</div>
    <div class="col bg-info text-white">Auto</div>
    <div class="col bg-success text-white">Auto</div>
  </div>
</div>

<!--
EXERCÍCIOS PRÁTICOS PARA PRATICAR O GRID:

1. Crie uma row com:
   - Uma coluna de 3
   - Uma de 6
   - Uma de 3

2. Crie uma seção responsiva:
   - Em telas pequenas (col-12): uma coluna por linha
   - Em telas médias (col-md-4): três colunas lado a lado

3. Monte um layout com sidebar:
   - Sidebar com col-md-3
   - Conteúdo principal com col-md-9

4. Crie uma galeria de 4 imagens por linha em telas grandes (lg), 2 por linha em telas médias (md), 1 por linha em pequenas (sm).

5. Faça uma linha com colunas de largura automática (col) e veja como se comportam.

6. Use alinhamentos com utilitários:
   - d-flex
   - justify-content-center
   - align-items-center

Dica final: Sempre aninhe colunas dentro de .row e .row dentro de .container.
-->