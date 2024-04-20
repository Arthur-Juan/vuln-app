from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configs.blueprints import register_blueprints
from flask_migrate import Migrate
from extensions import db   
from services import database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'bfc5221616fd29387d7413aeb41401391dceefa8'

db.init_app(app)

with app.app_context():
    from models.user import User
    from models.post import Post
    from models.comment import Comment


    db.create_all()

migrate = Migrate(app, db)

database.seed(db, app)


register_blueprints(app)


if __name__ == '__main__':
    app.run(debug=True)