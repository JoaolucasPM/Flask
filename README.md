# Conectando o flask ao banco de dados

Banco usado - SQLite3 [Documentação](https://sqlite.org/)

[Documentação Flask](https://flask.palletsprojects.com/en/stable/)

## Configuração do Projeto Flask

Este projeto utiliza o framework Flask para criar uma aplicação web básica. A estrutura e configuração da aplicação são definidas no arquivo principal. Abaixo, um resumo do funcionamento do código:

### Estrutura Básica

1. **Importação de Módulos**:
   - `os`: Para manipulação de caminhos e criação de pastas.
   - `Flask`: Para inicializar a aplicação web.

2. **Função `create_app`**:
   - Responsável por configurar e retornar a aplicação Flask.
   - Suporta configuração padrão e opcional para testes.

3. **Configurações Padrão**:
   - `SECRET_KEY`: Define uma chave de segurança padrão como 'dev'.
   - `DATABASE`: Localização do banco de dados SQLite (`instance/diobank.sqlite`).

4. **Carregamento de Configurações**:
   - Configurações adicionais podem ser carregadas de um arquivo `config.py` (se disponível).
   - Testes podem utilizar configurações específicas, passadas como parâmetro.

5. **Criação do Diretório de Instância**:
   - Garante que o diretório `instance/` existe, necessário para armazenar o banco de dados e outras configurações.

