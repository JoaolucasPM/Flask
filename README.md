# Criando um aplicação flask

[Documentação](https://flask.palletsprojects.com/en/stable/)


<h3>Orientação para que se use o ambiente virtual </h3>

# Criando o ambiente

```
python -m venv .venv
```

### Ativando o ambiente
```
.\venv\Scripts\Activate 
```
# Criando uma Aplicação Flask
### Instalando o flask

```
pip install flask
```
-  Criar um arquivo "app.py" e inserir o cód

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
``` 
- No terminar excecute 

```
flask --app run
```

Feito isso:


[Aplicação flask](http://127.0.0.1:5000)
