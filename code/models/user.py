from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    
    # fields that each user has
    uid      = db.Column(db.Integer, unique=True, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    
    # UserModel object constructor
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def json(self):
        return {
            "uid": self.uid,
            "username": self.username,
            "password": self.password
        }
    
    # save a record to the DB
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    # delete a record from the DB
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    # find a user by their username
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    # find a user by their uid
    @classmethod
    def find_by_uid(cls, uid):
        return cls.query.filter_by(uid=uid).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    
    def change_password(self, new_password):
        self.password = new_password
        db.session.commit()
        
        
    