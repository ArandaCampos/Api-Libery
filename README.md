## Api-Libery - Api para livros

![Badge de licença](http://img.shields.io/static/v1?label=LICENÇA&message=GNU&color=sucess&style=for-the-badge)   ![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=sucess&style=for-the-badge)   ![Badge versionamento](http://img.shields.io/static/v1?label=VERSAO&message=1.0&color=sucess&style=for-the-badge)

&emsp;O projeto criar uma forma prática e simples de controlar um estoque de livros. Permitindo criar, alterar, excluir e consultar dados.

## Modo de usar

    # Página Principal
    https://localhost:8000/api-auth
    
![pagina-principal-api-libary](https://user-images.githubusercontent.com/87876734/166554139-f0d5c212-cebb-4118-8954-4cbe47401ec9.png)

    # Inserir novos livros
    https://localhost:8000/api-auth/books

![inserir-api-libary](https://user-images.githubusercontent.com/87876734/166554156-c4df5347-f312-476c-9da1-add938a8e821.png)
    
    # Lista de livros cadastrados
    https://localhost:8000/api-auth/books
    
![lista-api-libary](https://user-images.githubusercontent.com/87876734/166554175-9e94ea9b-7dd0-4f94-bfdf-061648f564dc.png)

    # Editar, Remover, Alterar e Visualizar um livro específico cadastrado através do id
    https://localhost:8000/api-auth/books/<id>
![consulta-api-libary](https://user-images.githubusercontent.com/87876734/166554188-5670b89a-45ad-4e92-ae01-166541affb01.png)

## Tecnologias Empregadas

- Python
- Django
- API Rest
- SQLite

## Pré-requisitos

- Python3
- Virtualenv

## Instalação

    # Clonar o repositório
    $ git clone https://github.com/ArandaCampos/Api-Libery.git

    # Entrar no diretório
    $ cd Api-Libery

    # Criar o ambiente virtual
    $ virtualenv .
    $ source bin/activate

    # Instalar as dependências
    (Api-Libary) $ pip install -r requirements.txt
    
    # Habilitar o servidor
    (Api-Libary) $ python manage.py runserver
    
    # Abra o navegador de sua preferência e digite localhost:8000/api-auth/

E está pronto para usá-lo 💻
