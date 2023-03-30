from flask import Flask, render_template, url_for, redirect, request
from flask_login import login_required

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY=b'kristofer',
    SITE_NAME="ZIPCODE FORUM",
    SITE_DESCRIPTION="THE VOICE OF COOL DATA 40 COHORT",
    SQLALCHEMY_DATABASE_URI='sqlite:////tmp/database.db',
    SQLALCHEMY_ECHO=True
)


@app.route('/team')
def team():
    return render_template("team.html")


@app.route('/instructor')
def instructor():
    return render_template("instructor.html")


