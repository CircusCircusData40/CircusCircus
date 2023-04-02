from flask import render_template

from forum.app import app


@app.route('/bready')
def bready():
    return render_template("bready.html")
