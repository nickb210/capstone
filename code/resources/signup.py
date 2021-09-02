from flask_restful import Resource, reqparse
from models.user import UserModel
from resources.user import UserRegister
from flask import request, make_response, render_template, redirect, url_for

class SignUp(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="Username field cannot be left blank"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="Password field cannot be left blank."
    )
    
    
    @classmethod
    def get(cls):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("sign_up.html"), 200, headers)
    
    @classmethod
    def post(cls):
        data = SignUp.parser.parse_args()
        username = data["username"]
        password = data["password"]
        
        headers = {"Content-Type": "text/html"}
        #username = request.form.get("username")
        #password = request.form.get("password")
        
        if username == '' or password == '':
            return {"message": "username & password cannot be left blank"}, 400
        
        # create user
        user = UserModel(username, password)
        
        # hash user password
        user.hash_password(password)
        
        # check to see if user already exists
        if UserModel.find_by_username(user.username):
            return make_response(render_template("user_already_exists.html", user=user.username), 200, headers)
        
        user.save_to_db()
        return make_response(render_template("user_created_successful.html", user=user.username), 200, headers)
        