import os


class Config(object):

    # ENVIRONMENT
    ENV = 'development'
    # ENV = 'production'

    # DEBUG
    DEBUG = True

    # KEY
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # DATABASE
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:password@localhost/blog_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SECURITY
    SECURITY_PASSWORD_SALT = 'Hf}h7*nTioH;t358@7:#5V8NjrT7.9B!9Nq&%HFzFH^hy924nf2f)h(hEb,8O0>/{HgF<75DVi'
    SECURITY_PASSWORD_HASH = 'bcrypt'


# RUN IN TERMINAL
# export FLASK_APP=main.py
