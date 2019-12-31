import os


class Config(object):
    DEBUG = True

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:password@localhost/blog_flask'

    UPLOAD_FOLDER_IMAGE_POSTS = '/home/at/flask/app_blog/app/static/img/uploads_for_posts'
    ALLOWED_EXTENSIONS_IMAGE_POSTS = ["JPEG", "JPG", "PNG", "SVG", "GIF"]
    MAX_CONTENT_LENGTH_IMAGE_POSTS = 4 * 1024 * 1024

    # LANGUAGES = ['en', 'ru']
