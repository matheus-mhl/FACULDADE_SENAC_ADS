<!doctype html>
<html lang="pt-br">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>IA Template AV2</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-4Q6Gf2aSP4eDXB8Miphtr37CMZZQ5oXLH2yaXMJ2w8e2ZtHTl7GptT4jmndRuHDT" crossorigin="anonymous">
  <link rel="stylesheet" href="css/style.css" /> <!--Link para meu CSS-->
</head>

<body>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-j1CDi7MgGQ12Z7Qab0qlWQ/Qqz24Gc6BM0thvEMVjHnfYGF0rmFCozFSxQBxwHKO"
    crossorigin="anonymous">
  </script>

  <!--Construindo header-->
  <div class="container-fluid">
    <div class="row">
      <div class="col-12">
        <nav class="navbar navbar-expand-lg bg-white"> <!--Mudando a cor de fundo da barra de navegação-->
          <div class="container-fluid">
            <a class="navbar-brand" href="#">
              <img src="img/logo.png" alt="logo" style="padding-right:200px ;">
            </a>
            <!--Pesquisar barra-->
            <nav class="navbar bg-body-tertiary">
                <div class="container-fluid">
                  <form class="d-flex" role="search">
                    <button class="btn btn-outline-success" style="background-color: darkred; color: white" ype="submit">Buscar</button>
                  </form>
                </div>
              </nav>
            <!--Opções de navegação-->
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
              data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
              aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                <li class="nav-item">
                  <a class="nav-link active" style="color: black;" aria-current="page" href="#">HOME</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" style="color: black;" href="#">SOBRE</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" style="color: black;" href="#">ARTIFICIAL</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" style="color: black;" href="#">CONTATO</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    </div>
  </div>
  
  <!--Carrosel inicial da página-->
<div class="container-fluid">
  <div class="row">
    <div class="col-12">


      <div id="carouselExample" class="carousel slide">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="img/banner-01.jpg" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="img/banner-02.jpg" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="img/banner-03.jpg" class="d-block w-100" alt="...">
          </div>
        </div>
          <div class="carousel-item">
            <img src="img/banner-04.jpg" class="d-block w-100" alt="...">
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
      
        
    </div>
  </div>
</div>
  <!--Fim do banner-->

  <!--Conteúdo principal da página-->
  <div class="container bg-dark">
    <div class="row">
      <div class="col-6 col-md-6 d-flex" style="align-items: center;">
        <img src="img/ico-bola.png"> <h2 style="color: white;">FIFA, 21, 22 OU 23</h2>
      </div>
      <div class="col-6 col-md-8">
        <img src="img/Rectangle 2.jpg" alt="capa de jogador">
        <p style="color: white;">Lorem ipsum dolor sit amet consectetur adipisicing elit. Exercitationem soluta voluptatum autem rem sed, perferendis minima, facilis nostrum tenetur illum nihil similique repellendus odio? Tempore laboriosam quae similique sequi provident!</p>
        <div class="d-flex justify-content-between">
          <button type="button" class="btn btn-danger">JOGADORES</button>
          <button type="button" class="btn btn-danger">SELEÇÕES</button>
        </div>
      </div>
      <div class="col-6 col-md-4">
        <img src="img/ico-videogame.png"> <h2 style="color: white;">GAMERS</h2>
        <p style="color: white;">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Numquam incidunt libero sapiente ducimus voluptas error voluptate consequatur repellat! Iure in id distinctio ipsum nobis exercitationem magnam ipsam pariatur, quis delectus.</p>
        <h3 style="color: white;">SAIBA MAIS+</h3>
        <!--Segundo paragrafo-->
        <img src="img/ico-sistema.png"> <h2 style="color: white;">SISTEMA</h2>
        <p style="color: white;">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Numquam incidunt libero sapiente ducimus voluptas error voluptate consequatur repellat! Iure in id distinctio ipsum nobis exercitationem magnam ipsam pariatur, quis delectus.</p>
        <h3 style="color: white;">SAIBA MAIS+</h3>
      </div>
    </div>
    <!--ICONE CURIOSIDADES-->
    <div class="row">
      <div class="col-6 col-md-8 d-flex">
        <img src="img/ico-curiosidades.png" alt=""> <h2 style="color: white;">CURIOSIDADES</h2>
      </div>
    </div>
    <!--Accordeon-->
    <div class="row">
      <div class="col-12">
        

        <div class="accordion" id="accordionExample">
          <div class="accordion-item">
            <h2 class="accordion-header">
              <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne" style="background-color: grey; color: darkred; font-weight: bold;">
                FÉRIAS ME CONTA QUAL JOGO MAIS GOSTA?
              </button>
            </h2>
            <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
              <div class="accordion-body">
                <strong>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus commodi laudantium adipisci reprehenderit consectetur eius assumenda tempora cum dolorem sed, cumque suscipit a architecto. Est dolores natus eos atque ratione?
              </div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo" style="background-color: grey; color: darkred; font-weight: bold;" > 
                AINDA BAMOS APRENDER MUITA COISA BACANA
              </button>
            </h2>
            <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
              <div class="accordion-body">
                <strong>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus commodi laudantium adipisci reprehenderit consectetur eius assumenda tempora cum dolorem sed, cumque suscipit a architecto. Est dolores natus eos atque ratione?
              </div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree" style="background-color: grey; color: darkred; font-weight: bold;">
                NOS VEMOS SEMESTRE QUE VEM :-D
              </button>
            </h2>
            <div id="collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
              <div class="accordion-body">
                <strong>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus commodi laudantium adipisci reprehenderit consectetur eius assumenda tempora cum dolorem sed, cumque suscipit a architecto. Est dolores natus eos atque ratione?
              </div>
            </div>
          </div>
        </div>


      </div>
    </div>
  </div>
  </body>