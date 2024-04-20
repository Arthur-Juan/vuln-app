from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.post import Post
from models.user import User
from werkzeug.security import generate_password_hash

def seed(db: SQLAlchemy, app: Flask) -> None:
    with app.app_context(): 
        user_lsit = []
        user_lsit.append(User(name="Bob", email="bob@email.com", password=generate_password_hash("bob_pass"), is_admin=False))
        user_lsit.append(User(name="Admin", email="admin@email.com", password=generate_password_hash("adm_pass"), is_admin=True))

        for user in user_lsit:
            db.session.add(user)


        bob = User.query.filter_by(email="bob@email.com").first()
        post = Post(user_id=bob.id, content="first bost on this new blog", approved=True)
        db.session.add(post)
        db.session.commit()
        