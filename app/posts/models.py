import re
from datetime import datetime

from app import db


def slugify(st):
    pattern = r'[^\w+]'
    return re.sub(pattern, '+', st)


post_tags = db.Table('post_tags',
                     db.Column('post_id', db.Integer(), db.ForeignKey('post.id')),
                     db.Column('tag_id', db.Integer(), db.ForeignKey('tag.id'))
                     )


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(140))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    body = db.Column(db.Text())
    created_date = db.Column(db.DateTime, default=datetime.now())
    slug = db.Column(db.String(140), unique=True)

    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f'{self.title}'


class Tag(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)

    def __repr__(self):
        return f'{self.name}'
