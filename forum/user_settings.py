# trung's code
from flask import render_template, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, CHAR, Text
from sqlalchemy.orm import sessionmaker
from forum.app import app, db


@app.route('/comments')
def comments1():
    return render_template("comments.html")


@app.route('/team')
def team():
    return render_template("team.html")


@app.route('/instructor')
def instructor():
    return render_template("instructor.html")


# TO BYPASS ALL REQUEST
# @app.route("/usersetting")
# def usersetting():
#     return render_template("usersetting.html")


# class PersonalDetails(db.Model):
#     __user_setting__ = "details"
#
#     name = db.Column(db.String, primary_key=True)
#     email = db.Column(db.String)
#     gender = db.Column(db.String)
#     age = db.Column(db.Integer)
#     comments = db.Column(db.Text)
#
#     def __int__(self, name, email, gender, age, comments):
#         self.name = name
#         self.email = email
#         self.gender = gender
#         self.age = age
#         self.comments = comments
#
#     def __repr__(self):
#         return f"({self.name} {self.email} {self.gender} {self.age} {self.comments})"


# TRY TO MAKE DIFFERENT DATABASE TO SEE IF IT WORK
#
#


Base = declarative_base()


class PersonalDetails(Base):
    __tablename__ = "user"

    name = Column("name", String, primary_key=True)
    email = Column("email", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)
    comments = Column("comments", Text)

    def __int__(self, name, email, gender, age, comments):
        self._name = name
        self._email = email
        self._gender = gender
        self._age = age
        self._comments = comments

    def __repr__(self):
        return f"({self._name} {self._email} {self._gender} {self._age} {self._comments})"


engine = create_engine("sqlite:///trungdb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


# user1 = PersonalDetails("Trung","trung@trung.com","Male",23,"Nothing")
# session.add(user1)
# session.commit()
# WHY NOT WORK
# # @login_required
@app.route("/usersetting", methods=["GET", "POST"])
def usersetting():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        gender = request.form["gender"]
        age = request.form["age"]
        comments = request.form["comments"]

        # ERROR __INIT__ TAKE ONLY 1 ARGUMENT BUT 6 PROVIDED
        details = PersonalDetails(name, email, gender, age, comments)

        print(details)
        session.add(details)
        session.commit()
    else:
        return render_template("usersetting.html")

# for i in session.query(PersonalDetails):
#     print(i)
