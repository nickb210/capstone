from flask_restful import Resource, reqparse
from models.user import UserModel
from resources.user import UserRegister
from flask import request, make_response, render_template, redirect

class Login(Resource):
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
        return make_response(render_template("login.html"), 200, headers)
    
    @classmethod
    def post(cls):
        data = Login.parser.parse_args()
        username = data["username"]
        password = data["password"]
        
        headers = {"Content-Type": "text/html"}
        #username = request.form.get("username")
        #password = request.form.get("password")
        
        # check if fields are blank
        if username == '' or password == '':
            return {"message": "username & password cannot be left blank"}, 400
        
        # check to see if the user exsists
        user = UserModel.find_by_username(username)
        
        # if the user does not exists
        if not user:
            return {"message": "user '{}' does not exists".format(username)}, 400
        
        # check to see if password matches user credentials in DB.
        if user:
            # check to see if hashed password in db matches hashed password entered on page
            if not user.check_password(password):
                return {"message": "Incorrect password."}, 400
            
            return {"message": "logged in as '{}'.".format(user.username)}

    