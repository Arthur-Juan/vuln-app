from functools import wraps
from flask import request, abort
from flask import current_app, session
import models

def require_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("id"):
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            is_admin = session.get("is_admin")
            print(is_admin)
            if is_admin == False:
               return abort(403)
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500

        return f(*args, **kwargs)

    return decorated