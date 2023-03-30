# trung's code
from flask import render_template

from forum.app import app


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
