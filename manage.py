from app import manager, db
from app.posts import bp, models
from app.user import bp, models


if __name__ == '__main__':
    manager.run()
