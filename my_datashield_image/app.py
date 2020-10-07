import argparse

from flask import Flask, jsonify, request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/running', methods=['POST'])
def running():
    return render_template('running.html')

if __name__ == '__main__':

    ## parse arguments for debug mode
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--debug", action="store_true", help="debug flask")
    args = vars(ap.parse_args())

    if args["debug"]:
        app.run(debug=True, port=8080)
    else:
        app.run(host='0.0.0.0', threaded=True ,port=8080)

