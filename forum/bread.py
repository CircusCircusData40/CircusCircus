from flask import render_template

from forum.app import app


@app.route("/bread")
def bread():
    return render_template("bread.html")