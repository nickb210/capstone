from flask_restful import Resource, reqparse
from models.user import UserModel
from resources.user import UserRegister
from resources.change_password import ChangePassword
from flask import request, make_response, render_template, redirect, url_for, flash

class Home(Resource):
    @classmethod
    def get(cls):
        headers = {"Content-Type": "text/html"}
        
        # display /home endpoint page
        return make_response(render_template("main.html"), 200, headers)
        
    @classmethod
    def post(cls):
        headers = {"Content-Type": "text/html"}
        
        # Login as existing user.
        if request.form.get("login"):
            return redirect(url_for('login'))
              
        # Signup a User.
        elif request.form.get("sign_up"):
            return redirect(url_for('signup'))
        
        # user request to change password
        elif request.form.get("change_password"):
            return redirect(url_for('changepassword'))
            
        else:
            print("N/A")
        
        return make_response(render_template("main.html"), 200, headers)
        
        
