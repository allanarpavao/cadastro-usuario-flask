# StackUp - Backend

API para gerenciamento de usuários, desenvolvida com Flask, SQLAlchemy e Flask-OpenAPI3.  
Permite criar, listar, buscar e remover usuários de forma simples e estruturada.

## Instalação e Configuração

Siga as etapas abaixo para rodar o projeto localmente:

### Pré-requisitos

- Python 3.9 ou superior instalado
- Git instalado (opcional, para clonar o repositório)

### Instalação

1. **Clone o repositório (ou baixe os arquivos):**

```bash
git clone https://github.com/allanarpavao/cadastro-usuario-flask.git
```

2. **(Opcional) Crie um ambiente virtual:**

```bash
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Configure variáveis de ambiente, se necessário:**
- Exemplo: criar um arquivo `.env` com a variável `SECRET_KEY` ou outras configurações específicas.

5. **Inicie o servidor:**

```bash
python app.py
```

O backend estará disponível em `http://127.0.0.1:5000/`.

6. **Acesse a documentação interativa (Swagger):**
- Abra `http://127.0.0.1:5000/openapi` no navegador para visualizar e testar os endpoints da API.

## 🛠️ Tecnologias utilizadas

- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Flask-OpenAPI3](https://flask-openapi3.readthedocs.io/)
- [Flask-CORS](https://flask-cors.readthedocs.io/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
