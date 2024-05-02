from flask import Flask
import controllers
import controllers.admin_controller
import controllers.auth_controller
import controllers.home_controller
import controllers.posts_controller

def register_blueprints(app: Flask) -> None:
    try:
        app.register_blueprint(controllers.home_controller.home_controller)
        app.register_blueprint(controllers.auth_controller.auth_controller)
        app.register_blueprint(controllers.posts_controller.posts_controller)
        app.register_blueprint(controllers.admin_controller.admin_controller)

    except Exception as e:
        raise e
