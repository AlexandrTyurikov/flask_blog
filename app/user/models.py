from datetime import datetime

from flask_security import UserMixin, RoleMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login

roles_user = db.Table('roles_user',
                      db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                      db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
                      )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(80), unique=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    phone = db.Column(db.String(20))
    password = db.Column(db.String(120))
    active = db.Column(db.Boolean(), default=True)
    created_date = db.Column(db.DateTime, default=datetime.now())

    roles = db.relationship('Role', secondary=roles_user, backref=db.backref('users', lazy='dynamic'))

    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'{self.user_name}'


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text())

    def __repr__(self):
        return f'{self.name}'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
