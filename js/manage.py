from flask_script import Manager,Shell
from app import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()