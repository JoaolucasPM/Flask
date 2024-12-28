# API de Usuários com Flask

Este repositório contém uma API simples construída com Flask para gerenciar usuários. Ela permite criar novos usuários e listar todos os usuários existentes.

## Funcionalidades

- **Criar Usuário (POST)**: Adiciona um novo usuário ao banco de dados.
- **Listar Usuários (GET)**: Retorna todos os usuários cadastrados.

## Tutorial: Como Criar Cada Função

### 1. **Criando o Blueprint**

O **Blueprint** organiza a aplicação. Crie o Blueprint com o nome `user` e o prefixo de URL `/users`:

```python
from flask import Blueprint
app = Blueprint('user', __name__, url_prefix='/users')
```

### 2. **Função `_create_user()`**

Esta função cria um novo usuário:

```python
def _create_user():
    data = request.json
    user = User(username=data["username"])
    db.session.add(user)
    db.session.commit()
```

### 3. **Função `_list_users()`**

Esta função lista todos os usuários:

```python
def _list_users():
    query = db.select(User)
    users = db.session.execute(query).scalars()
    
    return [{'id': user.id, 'username': user.username} for user in users]
```

### 4. **Função `handle_user()`**

Gerencia as requisições `GET` e `POST`:

```python
@app.route('/', methods=['GET', 'POST'])
def handle_user():
    if request.method == 'POST':
        _create_user()
        return {'Post message': []}, HTTPStatus.CREATED
    else:
        return {'users': _list_users()}
```

### 5. **Configurando a Aplicação**

Registre o Blueprint na aplicação Flask principal:

```python
app = Flask(__name__)
app.register_blueprint(user_blueprint)
```

## Endpoints

### `POST /users/`

Cria um novo usuário com o nome fornecido no corpo da requisição.

### `GET /users/`

Lista todos os usuários cadastrados.



## Tecnologias Utilizadas

- Flask
- SQLAlchemy
- HTTPStatus

