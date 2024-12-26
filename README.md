# Definindo acesso ao banco

### Conforme a documentação do flask

Banco usado - SQLite3 [Documentação](https://sqlite.org/)

[Documentação Flask](https://flask.palletsprojects.com/en/stable/)

### Funções Principais

1. **`get_db`**:
   - Estabelece uma conexão com o banco de dados SQLite definido em `current_app.config['DATABASE']`.
   - Usa `sqlite3.Row` como fábrica de linhas, permitindo acessar os dados do banco como dicionários.
   - A conexão é armazenada no objeto global `g` para ser reutilizada durante o ciclo de requisição.

2. **`close_db`**:
   - Fecha a conexão com o banco de dados ao final de cada requisição.
   - Usa `g.pop('db')` para remover a conexão armazenada, caso exista.

3. **`init_db`**:
   - Inicializa o banco de dados executando os comandos definidos no arquivo `schema.sql`.
   - Usa o método `open_resource` de Flask para acessar o arquivo dentro do diretório da aplicação.

4. **`init_db_command`**:
   - Comando CLI para inicializar o banco de dados.
   - Apaga os dados existentes e recria as tabelas com base no schema definido.
   - Exemplo de uso:
     ```bash
     flask init-db
     ```

5. **`init_app`**:
   - Configura a aplicação Flask para:
     - Fechar a conexão com o banco automaticamente após o ciclo de requisição.
     - Registrar o comando CLI `init-db`.

### Modificação Necessária na Aplicação

Para que o banco de dados seja integrado corretamente à aplicação, é necessário importar e inicializar o módulo de banco de dados no arquivo principal:

```python
from . import db
db.init_app(app)