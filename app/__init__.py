from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_security import SQLAlchemyUserDatastore, Security

from config import Config
from app.admin import UserAdminView, RoleAdminView, HomeAdminView, PostAdminView, TagAdminView

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)


# ADMIN
from app.posts.models import *
from app.user.models import *

admin = Admin(app, 'JUNIOR DEVELOPER BLOG', url='/', index_view=HomeAdminView(name='Home'))

admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))
admin.add_view(UserAdminView(User, db.session))
admin.add_view(RoleAdminView(Role, db.session))


# BLUEPRINT
from app.posts import bp as post_bp
from app.user import bp as user_bp

app.register_blueprint(post_bp, url_prefix='/blog')
app.register_blueprint(user_bp, url_prefix='/user')


# FLASK SECURITY
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


from app import routes
# from app.posts import models
# from app.user import models
