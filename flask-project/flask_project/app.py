""" Sample Flask application """
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

global_books = {}

@app.route("/books", methods=["POST", "GET"])
def books():
    """ function to get and post books"""

    if request.method == 'GET':
        return jsonify(global_books), 200
    
    if request.method == 'POST':
        request_body = request.json
        global_books[request_body['id']] = request_body
        return jsonify(global_books), 200


@app.route("/books/<string:id>", methods=["GET"])
def get_book(id):
    """ view function to get the book with given id """
    if id in global_books:
        return jsonify(global_books[id]), 201
    else:
        return "document not found", 404


if __name__ == "__main__" :
    app.run()

