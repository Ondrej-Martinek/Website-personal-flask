from distutils.log import debug
import flask
from flask import request

app = flask.Flask(__name__)

json_table = {}

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return flask.render_template("index.html")
    elif request.method == 'POST':
        data = request.data
        print(data)
        return flask.render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)