from app import app, db
from app.models import Author, Books, Library

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Author": Author,
       "Books": Books,
       "Library": Library
   }