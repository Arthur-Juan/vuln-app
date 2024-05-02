from flask import Blueprint, jsonify, redirect, render_template, request
from models.post import Post
from extensions import db

from middleware.admin import require_admin
from sqlalchemy import or_

admin_controller = Blueprint('admin', __name__, template_folder='templates', url_prefix="/admin")

@admin_controller.get("/")
@require_admin
def admin_view():
    
    posts_to_approve = Post.query.filter(or_(Post.approved == False, Post.approved == None)).all()    
    
    return render_template("/pages/admin/index.html", posts=posts_to_approve)


@admin_controller.get("/approve/<post_id>")
@require_admin
def approve_view(post_id):
    post = Post.query.filter_by(id=post_id).first()

    if not post:
        return jsonify({"message": "post not found"}), 404
    
    return render_template("/pages/admin/approve.html", post=post)

@admin_controller.post("/approve/<post_id>")
@require_admin
def approve(post_id):
    approved = request.form.get("approved")
    approved = str_to_bool(approved)
    
    if type(approved) is not bool:
        return jsonify({"message":"only boolean values are allowed"})

    post = Post.query.filter_by(id=post_id).first()

    if not post:
        return jsonify({"message": "post not found"}), 404


    post.approved = approved
    db.session.commit()
    return redirect("/admin")    


def str_to_bool(value) -> bool:
    if value.lower() == "true":
        return True
    elif value.lower() == "false":
        return False
    else:
        raise ValueError("Invalid boolean string")