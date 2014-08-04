from flask import Blueprint, jsonify
from campering.users.models import User

users_app = Blueprint('users',__name__,template_folder='templates')

@users_app.route('/<userid>', methods = ['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is not None:
        return user
    return
