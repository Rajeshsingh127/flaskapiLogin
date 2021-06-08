from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
app  = Flask(__name__)
app.config['SECRET_KEY'] = "random secret key you wouldnt get it"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///login.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app,db)



from app import models,login
