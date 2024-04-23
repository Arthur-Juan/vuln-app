from flask import Blueprint, render_template, request

from models.post import Post


home_controller = Blueprint('home', __name__, template_folder='templates')

@home_controller.get("/")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(approved = True).paginate(page=page, per_page=5)
    if not posts:
        posts = []
    print(posts)
    return render_template("pages/home/index.html", posts=posts)