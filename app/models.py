from datetime import datetime
from app import db

class Author(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), index=True, unique=True)
   library = db.relationship("Library", backref="author", lazy="dynamic")

   def __str__(self):
       return f"<Author {self.name}>"

class Books(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   bookname = db.Column(db.Text)
   author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
   library = db.relationship("Library", backref="books", lazy="dynamic")


   def __str__(self):
       return f"<Books {self.id} {self.bookname[:50]} ...>"
   
class Library(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
   books_id = db.Column(db.Integer, db.ForeignKey('books.id'))
   available = db.Column(db.Text)
   borrowed = db.Column(db.Text)
   created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

   def __str__(self):
       return f"<Library {self.id} {self.author_id} {self.books_id[:50]} {self.available} {self.borrowed}...>"
   