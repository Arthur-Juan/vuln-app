from flask import Blueprint, render_template

from models.post import Post


home_controller = Blueprint('home', __name__, template_folder='templates')

@home_controller.get("/")
def home():

    posts = Post.query.filter_by(approved = True).all()
    if not posts:
        posts = []
    print(posts)
    return render_template("pages/home/index.html", posts=posts)