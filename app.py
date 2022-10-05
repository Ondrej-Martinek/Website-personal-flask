from flask import Flask, request, render_template, url_for

app = Flask(__name__)

json_table = {}

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        data = request.data
        print(data)
        #render_template("index.html", data=data)
        return url_for(index) 
'''
@app.route("/secondPage")
def secondPage():
'''

if __name__ == "__main__":
    app.run(host='0.0.0.0')
