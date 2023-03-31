# trung's code
from flask import render_template, request

from forum.app import app, db
# from forum.models import PersonalDetails


@app.route('/team')
def team():
    return render_template("team.html")


@app.route('/instructor')
def instructor():
    return render_template("instructor.html")


# TO BYPASS ALL REQUEST
@app.route("/usersetting")
def user_setting():
    return render_template("usersetting.html")

#
#NOT WORK
# # @login_required
# @app.route("/usersetting", method=["POST"])
# def usersetting():
#     if request.method == "POST":
#         name = request.form["name"]
#         email = request.form["email"]
#         gender = request.form["gender"]
#         age = request.form["age"]
#         comments = request.form["comments"]
#
#         details = PersonalDetails(name, email, gender, age, comments)
#         db.session.add(details)
#         db.session.commit()
#     else:
#         return render_template("usersetting.html")

# THIS DOES NOT WORK
# conn = sqlite3.connect('database.db')
# c = conn.cursor()
# c.execute("Insert into User", (name, email, gender, age, comments))
# conn.commit()
# conn.close()
