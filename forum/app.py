from flask import Flask

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY=b'kristofer',
	SITE_NAME = "ZIPCODE FORUM",
	SITE_DESCRIPTION = "THE VOICE OF COOL DATA 40 COHORT",
	SQLALCHEMY_DATABASE_URI='sqlite:////tmp/database.db',
	SQLALCHEMY_ECHO=True
)
