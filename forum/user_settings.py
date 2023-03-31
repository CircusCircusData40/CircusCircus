# trung's code
from flask import render_template, request

from forum.app import app, db


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


# WHY NOT WORK
# # @login_required
# @app.route("/usersetting", methods=["POST"]) <<<<<<<<<<THIS CAUSE BREAK
# def usersetting():
#     if request.method == "POST":
#         name = request.form["name"]
#         email = request.form["email"]
#         gender = request.form["gender"]
#         age = request.form["age"]
#         comments = request.form["comments"]
#
    #     details = PersonalDetails(name, email, gender, age, comments)
    #     db.session.add(details)
    #     db.session.commit()
    # else:
    #     return render_template("usersetting.html")


# THIS DOES NOT WORK
# conn = sqlite3.connect('database.db')
# c = conn.cursor()
# c.execute("Insert into User", (name, email, gender, age, comments))
# conn.commit()
# conn.close()


# NOT WORK
# class PersonalDetails(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     email = db.Column(db.String)
#     gender = db.Column(db.String)
#     age = db.Column(db.Integer)
#     comments = db.Column(db.Text)
#
# #
#     def __int__(self, name, email, gender, age, comments):
#         self.name = name
#         self.email = email
#         self.gender = gender
#         self.age = age
#         self.comments = comments
#
