from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.post import Post
from models.user import User
from werkzeug.security import generate_password_hash

def seed(db: SQLAlchemy, app: Flask) -> None:
    with app.app_context():
        user_list = []
        # Check if the user already exists before adding them
        if not User.query.filter_by(email="bob@email.com").first():
            user_list.append(User(name="Bob", email="bob@email.com", password=generate_password_hash("bob_pass"), is_admin=False))
        if not User.query.filter_by(email="admin@email.com").first():
            user_list.append(User(name="Admin", email="admin@email.com", password=generate_password_hash("adm_pass"), is_admin=True))

        for user in user_list:
            db.session.add(user)

        bob = User.query.filter_by(email="bob@email.com").first()
        # Check if the post already exists before adding it
        if not Post.query.filter_by(user_id=bob.id,title="first post!!", content="first post on this new blog").first():
            post = Post(user_id=bob.id, title="first post!!", content="first post on this new blog", approved=True)
            db.session.add(post)
        
        db.session.commit()
        