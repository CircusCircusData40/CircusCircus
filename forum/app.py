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

print("app.config")


@app.route('/team')
def team():
    return render_template("team.html")


@app.route('/instructor')
def instructor():
    return render_template("instructor.html")


# @login_required
@app.route('/usersettings', methods=["POST"])
def user_submit():
    # if request.method == "POST":
    #     name = request.form['name']
    #     email = request.form['email']
    #     gender = request.form['gender']
    #     age = request.form['age']
    #     comments = request.form['comments']
    #     details = [name, email, gender, age, comments]
        # conn = sqlite3.connect('database.db')
        # c = conn.cursor()
        # c.execute("Insert into User", (name, email, gender, age, comments))
        # conn.commit()
        # conn.close()

        # db.session.add(details)
        # db.session.commit()
    # else:
    return render_template("usersettings.html")

# @login_required
# @app.route('/usersettings', methods=["POST"])
# def photo_upload():
#     if request.method == "POST":
#         photo = request.form["photo"]
# conn = sqlite3.connect('database.db')
# c = conn.cursor()
# c.execute("Insert Photo into User", photo)
# conn.commit()
# conn.close()
#
# db.session.add(photo)
# db.session.commit()
# else:
#     return render_template("usersettings.html")
