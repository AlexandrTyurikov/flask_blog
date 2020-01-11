from flask import Blueprint

bp = Blueprint('user_u', __name__, template_folder='templates')

from app.user import routes
