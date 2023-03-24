from flask import Flask
import db
import auth

VERSION = "1"

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/get_mem")
def mem():
    return "<p>Заходят значит 3 еврея в бар...</p>"