from forum.app import app
from forum.object_models import *
from flask_login.login_manager import LoginManager

# adding db url
import os

if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    print("setting db url for postgres")
else:
    print("DATABASE_URL is not set, using sqlite")

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


# DATABASE STUFF
@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)


password_regex = re.compile("^[a-zA-Z0-9!@#%&]{6,40}$")
username_regex = re.compile("^[a-zA-Z0-9!@#%&]{4,40}$")


# Account checks
def username_taken(username):
    return User.query.filter(User.username == username).first()


def email_taken(email):
    return User.query.filter(User.email == email).first()


def valid_username(username):
    if not username_regex.match(username):
        # username does not meet password reqirements
        return False
    # username is not taken and does meet the password requirements
    return True


def valid_password(password):
    return password_regex.match(password)


# Post checks
def valid_title(title):
    return len(title) > 4 and len(title) < 140


def valid_content(content):
    return len(content) > 10 and len(content) < 5000
