from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def hello_world():
    return "Zip Code Rocks!"

app.run('127.0.0.1', port=5001)