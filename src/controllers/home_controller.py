from flask import Blueprint, render_template


home_controller = Blueprint('home', __name__, template_folder='templates')

@home_controller.get("/")
def home():
    return render_template("pages/home/index.html")