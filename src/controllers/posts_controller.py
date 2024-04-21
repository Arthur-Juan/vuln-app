from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from extensions import db
from models.post import Post

posts_controller = Blueprint('posts', __name__, template_folder='templates', url_prefix="/posts")


@posts_controller.get("/")
def get_posts():
    
    posts = Post.query.filter_by(approved = True).all()
    if not posts:
        return jsonify({
            "message":"Posts no found"
        }), 404

    print(posts)
    return jsonify(posts), 200
    pass