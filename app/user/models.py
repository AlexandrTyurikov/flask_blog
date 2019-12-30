from datetime import datetime

from flask_security import UserMixin, RoleMixin

from app import db

roles_user = db.Table('roles_user',
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                      db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
                      )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    phone = db.Column(db.String(20))
    password = db.Column(db.String(120))
    active = db.Column(db.Boolean)

    role = db.relationship('Role', secondary=roles_user, backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text)
