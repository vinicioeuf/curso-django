# Controle de Estoque

![Badge em Desenvolvimento](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

## Índice

- [Descrição](#descri%C3%A7%C3%A3o)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instala%C3%A7%C3%A3o)
- [Como Usar](#como-usar)
- [Contribuição](#contribui%C3%A7%C3%A3o)
- [Licença](#licen%C3%A7a)
- [Contato](#contato)

## Descrição

O **Controle de Estoque** é um projeto desenvolvido como parte do curso de Django no IFSertãoPE Campus Salgueiro. Este sistema permite gerenciar produtos, fornecedores, movimentações de estoque e categorias, proporcionando uma visão clara e organizada do inventário.

## Funcionalidades

- Cadastro de produtos
- Gerenciamento de fornecedores
- Registro de movimentações de entrada e saída
- Classificação de produtos por categorias
- Relatórios de estoque atualizados

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [SQLite](https://www.sqlite.org/index.html)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/vinicioeuf/curso-django.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd curso-django
   ```

3. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   ```

4. Ative o ambiente virtual:

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

   - No Linux/Mac:

     ```bash
     source venv/bin/activate
     ```

5. Instale as dependências:

   ```bash
   pip install -r requisitos.txt
   ```

6. Realize as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

7. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

## Como Usar

- Acesse o sistema através do navegador em `http://127.0.0.1:8000/`.
- Utilize o menu lateral para navegar entre as funcionalidades.
- Cadastre produtos, fornecedores, categorias e registre movimentações conforme necessário.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

- **Nome:** Vinício Eufrásio
- **Instituição:** IFSertãoPE Campus Salgueiro
- **E-mail:** [vinicio.eufrazio@aluno.ifsertão-pe.edu.br](mailto:vinicio.eufrazio@aluno.ifsertão-pe.edu.br)
- **LinkedIn:** [Vinicio Eufrazio - Desenvolvedor web (PHP, Django) e Mobile (Flutter)](https://www.linkedin.com/in/vinicio-eufrazio-8a64a61a3/)