from flask import Blueprint, request
from src.app import User, db
from http import HTTPStatus
# __name__ = caminho do arquivo

app =  Blueprint('user', __name__,url_prefix='/users')

def _create_user():
    data = request.json 
    user =  User(username=data["username"])
    db.session.add(user)
    db.session.commit()

def _list_users():
    query = db.select(User)
    users  = db.session.execute(query).scalars()
    
    return [
        {
            'id': user.id ,
            'username': user.username,
        } 
        for user in users
    ]

@app.route('/', methods=['GET', 'POST'])
def handle_user():
    if request.method == 'POST':
        _create_user()
        return {'Post message': []}, HTTPStatus.CREATED
    else:
        return {'users': _list_users()}
    

    