from flask import Flask
from controllers.home_controller import home_controller

def register_blueprints(app: Flask) -> None:
    try:
        app.register_blueprint(home_controller)
    except Exception as e:
        raise e
