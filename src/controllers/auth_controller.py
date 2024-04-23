from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db

auth_controller = Blueprint('auth', __name__, template_folder='templates')

@auth_controller.get("/register")
def register_view():
    if session.get("id"):
             return redirect("/")
    return render_template("pages/auth/register.html")

@auth_controller.post("/register")
def register():
    
    data = request.json
    email = data.get("email")
    name = data.get("name")
    password = data.get("password")
        
    user = User.query.filter_by(email=email).first();
    if user:
        return jsonify({
            "success": False,
            "message": "User Already Exists" 
        }), 400
    
    new_user = User(name=name, email=email, password=generate_password_hash(password), is_admin=False)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("auth.login_view"))    

@auth_controller.get("/login") 
def login_view():
        if session.get("id"):
             return redirect("/")
              
        return render_template("pages/auth/login.html")

@auth_controller.post("/login")
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password=password):
          return jsonify({
               "success": False,
               "message": "invalid credentials"
          }), 400 
    session["id"] = user.id
    session["email"] = user.email
    session["name"] = user.name
    session["is_admin"] = user.is_admin
    return redirect("/")
