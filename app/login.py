from app import app,db
from flask import jsonify,request
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash

@app.route("/signup", methods = ['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'])
    try:
        user =  User(username=data["username"],password = hashed_password,email = data["email"])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "user has been created"})
    except:
        return jsonify({"message": "Username or email is taken"})


@app.route("/login",methods = ['POST'])
def login():
    data  = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user is not None and check_password_hash(user.password,data["password"]):
        return jsonify(message ="welcome",
                       username= user.username,
                       email = user.email)
    else:
        return jsonify(({"message":"credential are invalid"}))



