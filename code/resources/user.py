from flask_restful import Resource, reqparse
from models.user import UserModel
from flask import request, make_response, render_template, redirect

USER_ALREADY_EXISTS       = "Username '{}' is already taken."
UID_NOT_FOUND             = "A user with uid:'{}' not found."
USER_CREATED_SUCCESSFULLY = "User '{}' created successfully."
USER_DELETED              = "User with UID '{}' deleted."

class UserRegister(Resource):
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
    
    def post(self):
        data = UserRegister.parser.parse_args()
        username = data["username"]
        password = data["password"] 
        
        # check to see if a username is taken
        if UserModel.find_by_username(username):
            return {"message": USER_ALREADY_EXISTS.format(username)}, 400
        
        """
        since the username is not taken, create a User object and save 
        it to the DB.
        """
        user = UserModel(username, password)
        user.save_to_db()
        
        return {"message": USER_CREATED_SUCCESSFULLY.format(username)}, 201
    
    
class User(Resource):
    @classmethod
    def get(cls, uid):
        user = UserModel.find_by_uid(uid)
        
        if not user:
            return {"message": UID_NOT_FOUND.format(uid)}, 404
        return user.json()

    @classmethod
    def delete(cls, uid):
        user = UserModel.find_by_uid(uid)
        
        if not user:
            return {"message": UID_NOT_FOUND.format(uid)}, 404
        
        user.delete_from_db()
        return {"message": USER_DELETED.format(uid)}

# Return all users that have accounts
class UserList(Resource):
    @classmethod
    def get(cls):
        return {"user_list": [user.json() for user in UserModel.query.all() ]}