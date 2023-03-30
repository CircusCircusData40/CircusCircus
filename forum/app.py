from flask import Flask, render_template, url_for, redirect, request

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


@app.route('/usersettings', methods=["POST", "GET"])
def usersettings():
    # if request.method == "POST":
    #     name = request.form[name]
    #     email = request.form[email]
    #     gender = request.form[gender]
    #     age = request.form[age]
    #     comments = request.form[comments]
    #
    # else:
        return render_template("usersettings.html")
