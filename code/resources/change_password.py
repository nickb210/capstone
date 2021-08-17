from flask_restful import Resource, reqparse
from models.user import UserModel
from resources.user import UserRegister
from flask import request, make_response, render_template, redirect

class ChangePassword(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="Username field cannot be left blank"
    )
    parser.add_argument(
        'old_password',
        type=str,
        required=True,
        help="old Password field cannot be left blank."
    )
    parser.add_argument(
        'new_password',
        type=str,
        required=True,
        help="new Password field cannot be left blank."
    )
    
    
    @classmethod
    def get(cls):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("change_password.html"), 200, headers)
    
    @classmethod
    def post(cls):
        data = ChangePassword.parser.parse_args()
        
        username     = data["username"]
        old_password = data["old_password"]
        new_password = data["new_password"]
        
        #username = request.form.get("username")
        #old_password = request.form.get("old_password")
        #new_password = request.form.get("new_password")
        

        user = UserModel.find_by_username(username)
        
        # if the user does not exists
        if not user:
            return {"message": "user '{}' does not exists".format(username)}, 400
        
        # if the current password does not match
        if user.password != old_password:
            return {"message": "password does not match your old password"}, 404
        
        user.change_password(new_password)
        return {"message": "success. Changed password from '{}' to '{}'".format(old_password, new_password)}, 200
        
        