from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configs.blueprints import register_blueprints
from flask_migrate import Migrate
from models.user import User
from models.post import Post
from models.comment import Comment
from extensions import db   

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate(app, db)


register_blueprints(app)


if __name__ == '__main__':
    app.run(debug=True)