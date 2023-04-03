import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY=b'kristofer',
    SITE_NAME="ZIPCODE DATA 4.0 FORUM",
    SITE_DESCRIPTION="THE VOICE OF COOL DATA 40 COHORT",
    SQLALCHEMY_DATABASE_URI='sqlite:///database.db',
    SQLALCHEMY_ECHO=True
)

login_manager = LoginManager()
login_manager.init_app(app)


print("app.config done.")

if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    print("setting db url for postgres")
else:
    print("DATABASE_URL is not set, using sqlite")
db = SQLAlchemy(app)
print("SQLAlchemy init.")
print('checking for database')
