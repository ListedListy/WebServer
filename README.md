# WebServer Social

Projeto final de Administracao de Sistemas II.

Aplicacao Django simples com tres paginas principais:

- pagina inicial com publicacoes;
- pagina de utilizadores;
- pagina com as publicacoes de um utilizador.

Os dados sao guardados em base de dados atraves dos modelos `Profile`, `Post` e `Comment`.

## Tecnologias

- Python
- Django
- MySQL
- Docker
- Docker Compose
- Variaveis de ambiente com `python-dotenv`

## Desenvolvimento local

Criar e ativar o ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Copiar o ficheiro de exemplo de variaveis de ambiente:

```bash
copy .env.example .env
```

Para desenvolvimento local sem Docker, usar SQLite:

```env
DB_ENGINE=sqlite
```

Aplicar migracoes:

```bash
python manage.py migrate
```

Iniciar a aplicacao:

```bash
python manage.py runserver
```

A aplicacao fica disponivel em:

```text
http://127.0.0.1:8000/
```

## Docker Compose

Copiar o ficheiro de ambiente:

```bash
copy .env.example .env
```

Atualizar as passwords no ficheiro `.env` e iniciar os servicos:

```bash
docker compose up --build
```

Servicos configurados:

- `web`: aplicacao Django;
- `db`: base de dados MySQL.

## Variaveis de ambiente

O ficheiro `.env` nao deve ser enviado para o Git. O repositório inclui apenas `.env.example`.

Principais variaveis:

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `TIME_ZONE`
- `DB_ENGINE`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
- `MYSQL_ROOT_PASSWORD`

## Ambientes

Em desenvolvimento local, pode ser usado SQLite com `DB_ENGINE=sqlite`.

Em Docker/produção, deve ser usado MySQL com:

```env
DB_ENGINE=mysql
DB_HOST=db
DEBUG=False
```

Tambem devem ser configurados valores seguros para `SECRET_KEY`, `DB_PASSWORD` e `MYSQL_ROOT_PASSWORD`.

## Commits dos requisitos

- `Inicio do projeto Django`
- `Configuração do ambiente virtual e dependências`
- `Criação da aplicação principal Django`
- `Desenvolvimento das páginas principais`
- `Criação dos modelos e ligação à base de dados`
- `Configuração das variáveis de ambiente`
- `Configuração da base de dados MySQL`
- `Configuração do Dockerfile`
- `Configuração do Docker Compose`
- `Ajustes finais e documentação`
