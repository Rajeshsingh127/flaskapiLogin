from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(500))
    email = db.Column(db.String(120),unique=True)
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
    def __repr__(self):
        return self.username
