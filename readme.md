<h1>Repositório Universitário</h1>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=python&message=3.9.0&color=3776AB&style=for-the-badge&logo=PYTHON"/>
  <img src="https://img.shields.io/static/v1?label=Heroku&message=deploy&color=430098&style=for-the-badge&logo=heroku"/>
  <img src="http://img.shields.io/static/v1?label=License&message=MIT&color=green&style=for-the-badge"/>
  <img src="http://img.shields.io/static/v1?label=Django&message=3.1.x&color=092E20&style=for-the-badge&logo=Django"/>
  <img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=green&style=for-the-badge"/>
</p>

### :checkered_flag: Tópicos 

:pushpin: [Descrição do projeto](#descrição-do-projeto)

:pushpin: [Funcionalidades](#funcionalidades)

:pushpin: [Deploy da Aplicação](#deploy-da-aplicação)

:pushpin: [Pré-requisitos](#pré-requisitos)

:pushpin: [Como rodar a aplicação](#como-rodar-a-aplicação)

## Descrição do Projeto
<p align="justify">
  Projeto base de um repositório universtirário, com artigos, monografias, dissertações e demais produções acadêmicas.
  Foi desenvolvido somente o básico com o upload dos arquivos e acesso somente de administrador.
  A pesquisa deve ser melhor implementada. 
</p>

## Funcionalidades
:white_check_mark: Acesso ao painel somente para usuário admin
:white_check_mark: Upload de arquivos
:white_check_mark: Pesquisa com elementos avançados

## Deploy da aplicação
* [Heroku](https://django-repositorio-im.herokuapp.com/)

* Para fazer login: 
    * digite: `/login` ou 
    * acesse [aqui](https://django-repositorio-im.herokuapp.com/login)

* Credenciais:
    * username: teste@testador.com
    * password: 12345678

## Pré Requisitos
* [Django 3.1](https://www.djangoproject.com/)

## Como rodar a aplicação
1. Clone o projeto

    git clone https://github.com/Italo11Marcos/repositorio-universitario.git

    2. Crie um virtualenv
    
    virtualenv venv --python=3.x.x

    3. Ative o seu virtualenv. 

    source venv/bin/activate

    4. Instale dependências

    pip3 -r install requirements.txt

    5. Crie as migrations

        * python3 manage.py makemigrations
        * python3 manage.py migrate
    
    6. Usuário admin: 
        
        * username: teste@testador.com
        * password: 12345678

    7. Caso queira criar seu próprio user admin

    python3 manage.py createsuperuser

    8. Execute o projeto

    python3 manage.py runserver

## Pacotes e bibliotecas utilizadas
* [Bootstrap 4.5](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
* [JQuery 3.5.1](https://jquery.com/)
* [Font Awesome](https://fontawesome.com/)
* [AdminLTE 3](https://adminlte.io/docs/3.0/)

