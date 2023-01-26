from flask import request, jsonify

from models.book import Author, Book
from schemas.book_schema import AuthorSchema, BookSchema
from database import db
def all_books():
    author = Author.query.all()
    author_schema = AuthorSchema(many=True)
    return (author_schema.dump(author), 200)

def read_one(id):
    author = Author.query.get(id)
    author_schema = AuthorSchema()
    return (author_schema.dump(author), 200)
    
def create():
    author_schema = AuthorSchema()
    author = Author(name=request.json.get('name'))
    book = Book(title=request.json.get('title'), author=author)
    db.session.add(author)
    db.session.add(book)
    db.session.commit()
    return (author_schema.dump(author), 200)

def update(id):
    get_author = Author.query.get(id)
    if request.json.get('name'):
        get_author.name = request.json.get('name')

    if request.json.get('title'):
        get_author.title = request.json.get('title')
    
    db.session.add(get_author)
    db.session.commit()
    author_schema = AuthorSchema()
    return (author_schema.dump(get_author), 200)

def delete(id):
    get_author = Author.query.get(id)   
    db.session.delete(get_author)
    db.session.commit()
    author_schema = AuthorSchema()
    return (author_schema.dump(get_author), 200)