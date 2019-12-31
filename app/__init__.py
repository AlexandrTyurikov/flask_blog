from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# from app.user.models import User, Role
from app.posts.models import Post, Tag

admin = Admin(app)
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Tag, db.session))

from app.posts import bp as post_bp
from app.user import bp as user_bp

app.register_blueprint(post_bp, url_prefix='/blog')
app.register_blueprint(user_bp, url_prefix='/user')

from app import routes
