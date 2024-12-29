# Gerenciando migrações com Alembic 

[Alembic](https://flask-migrate.readthedocs.io/en/latest/) é uma extensão para gerenciar migrações de banco de dados em aplicações Flask.

## Instalação
Para inicializar o uso do Alembic em seu projeto Flask, execute o seguinte comando no terminal:

```bash
flask db init
```

## Configuração no arquivo ```app.py```
Adicione a integração com o Flask-Migrate no arquivo principal do seu aplicativo:

```python
from flask_migrate import Migrate
migrate = Migrate(app, db)
```

Certifique-se de que a variável `app` é a instância do Flask e `db` é a instância do SQLAlchemy.

## Gerando uma migração
Para criar um arquivo de migração com as alterações realizadas no modelo de dados, use o seguinte comando:

```bash
flask db migrate -m "Initial migration."
```

Substitua o texto entre aspas por uma descrição significativa sobre a migração.

## Aplicando alterações no banco de dados
Depois de gerar a migração, aplique as alterações ao banco de dados com o comando:

```bash
flask db upgrade
```

Este comando atualiza o esquema do banco de dados com base nas migrações geradas.


