from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from extensions import db
from models.post import Post
from models.user import User

posts_controller = Blueprint('posts', __name__, template_folder='templates', url_prefix="/posts")


@posts_controller.post("/")
def create_post():
    
    data = request.form
    title = data.get("title")
    content = data.get("content")

    if not session.get("id"):
        return redirect("/login")
    
    user = User.query.filter_by(id=session.get("id")).first()
    if not user:
        return redirect("/login")
    
    post = Post(user_id=user.id, title=title, content=content, banner=None, approved=False)
    db.session.add(post)
    db.session.commit()
    return redirect(f"/posts/{post.id}")


@posts_controller.get("/<post_id>") 
def get_post(post_id) -> str :
    post = Post.query.filter_by(id = post_id).first()
    if not post:
        return jsonify(
            {"message": "no post with this id"}
        ), 404
    
    if post.approved == False and session.get("id") != post.user_id:
        return jsonify(
            {"message": "you cannot view this post"}

        ), 401
    
    
    return render_template("pages/posts/detail.html", post=post, session_id=session.get("id"))
    
@posts_controller.get("/<post_id>/edit")
def edit_post_view(post_id):
    post = Post.query.filter_by(id = post_id).first()
    if not post:
        return jsonify(
            {"message": "no post with this id"}
        ), 404
    
    if session.get("id") != post.user_id:
        return jsonify(
            {"message": "you cannot view this post"}

        ), 401
    
    
    return render_template("pages/posts/edit.html", post=post, session_id=session.get("id"))
    
@posts_controller.post("/<post_id>/edit")
def edit_post(post_id) -> str:
    data = request.form
    title = data.get("title")
    content = data.get("content")

    post = Post.query.filter_by(id = post_id).first()
    post.title = title
    post.content = content
    db.session.commit()
    return redirect(f"/posts/{post.id}")
