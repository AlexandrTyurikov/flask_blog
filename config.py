import os


class Config(object):
    ENV = 'development'
    # ENV = 'production'

    DEBUG = True

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:password@localhost/blog_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
