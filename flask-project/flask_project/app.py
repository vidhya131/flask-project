""" Sample Flask application """
from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_all_books():
    """ function to get all the books"""
    return "hello world"
