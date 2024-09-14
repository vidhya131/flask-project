""" Sample Flask application """
from flask import Flask, jsonify, request
from mysql_connection import MySQLConnection

app = Flask(__name__)

con_obj = MySQLConnection(
        host='sql12.freesqldatabase.com',
        user='sql12730238',
        password='6hWrY8SfEY',
        database='sql12730238'
    )

@app.route("/books", methods=["GET"])
def get_all_books():
    """ view function to get all books """

    cursor = con_obj.get_cursor()
    query = "SELECT * FROM books"
    cursor.execute(query)
    results = cursor.fetchall()  # Fetch all rows
    con_obj.close()
    return jsonify(results), 200


@app.route("/books", methods=["POST"])
def add_book():
    """ adds a book to books table"""
    # Get JSON data from the request
    data = request.get_json()
    cursor = con_obj.get_cursor()
    # Check if data is received
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # todo: validate schema
    author = data.get("author")
    title = data.get("title")
    id = data.get("id")
    insert_query = "INSERT INTO books (id, author, title) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (id,author, title))
    con_obj.connection.commit()
    con_obj.close()

    # Process the data (this is just a simple example)
    processed_data = {
        'received_data': data,
        'message': 'Record ingested successfully!'
    }

    # Return a JSON response
    return jsonify(processed_data), 200


@app.route("/books/<string:id>", methods=["GET"])
def get_book(id):
    """ view function to get the book with given id """
    query = "select * from books where id = %s"

    cursor = con_obj.get_cursor()

    cursor.execute(query, (id,))

    if cursor.fetchone():
        return jsonify(cursor.fetchone()), 201
    else:
        return f"document with id : {id} not found", 404


if __name__ == "__main__" :
    app.run()

