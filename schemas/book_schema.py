from marshmallow import Schema, fields, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.book import Author, Book
class AuthorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        include_relationships = True
        load_instance = True


class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        include_fk = True
        load_instance = True