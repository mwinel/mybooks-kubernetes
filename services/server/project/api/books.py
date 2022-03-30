import os

from flask import Flask, Blueprint, jsonify, request

from project.api.models import Book
from project import db

app = Flask(__name__)

books_blueprint = Blueprint('books', __name__)

@books_blueprint.route('/api/v1/books', methods=['GET', 'POST'])
def all_books():
    response_object = {
        "status": "success",
    }

    if request.method == 'POST':
        post_data = request.get_json()
        title = post_data.get('title')
        author = post_data.get('author')
        db.session.add(Book(title=title, author=author))
        db.session.commit()
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = [book.serialize() for book in Book.query.all()]
    return jsonify(response_object)

@books_blueprint.route('/api/v1/books/<book_id>', methods=['GET', 'PATCH', 'DELETE'])
def single_book(book_id):
    response_object = {
        "status": "success",
    }
    if request.method == 'GET':
        book = Book.query.filter_by(id=book_id).first()
        if book:
            response_object['book'] = book.serialize()
            return jsonify(response_object)
        else:
            response_object['message'] = 'Book not found'
            return jsonify(response_object), 404

    if request.method == 'PATCH':
        book = Book.query.filter_by(id=book_id).first()
        if book:
            post_data = request.get_json()
            book.title = post_data.get('title')
            book.author = post_data.get('author')
            db.session.commit()
            response_object['message'] = 'Book successfully updated!'
        else:
            response_object['message'] = 'Book not found'
            return jsonify(response_object), 404

    if request.method == 'DELETE':
        book = Book.query.filter_by(id=book_id).first()
        if book:
            db.session.delete(book)
            db.session.commit()
            response_object['message'] = 'Book successfully deleted!'
        else:
            response_object['message'] = 'Book not found'
            return jsonify(response_object), 404
   
    return jsonify(response_object)

@books_blueprint.route('/api/v1/status', methods=['GET'])
def health_check():
    return jsonify({'status': 'success', 'message': 'OK - healthy'})

# if __name__ == '__main__':
#     app.run()