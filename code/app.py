#!/usr/bin/env python3
from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister, User, UserList
from resources.home import Home
from resources.change_password import ChangePassword
from resources.signup import SignUp
from resources.login import Login
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']         = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
app.config['PROPAGATE_EXCEPTIONS']            = True

app.secret_key = 'nick'

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

# API resrouces
api.add_resource(Home, '/home')
api.add_resource(ChangePassword, '/changepassword')
api.add_resource(SignUp, '/signup')
api.add_resource(Login, '/login')

api.add_resource(UserList, '/users')
api.add_resource(User, '/user/<int:uid>')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    #app.run(port=4444, debug=True)
    app.run(host="0.0.0.0", port=80, debug=True)