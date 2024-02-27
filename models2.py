import json

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

     
    def borrowed(self):
        
      if self.available:
            self.available = False
            print(f"Książka '{self.title}' została wypożyczona.")
      else:
            print(f"Książka '{self.title}' jest dostepna.")

    
    def returned(self):
        self.available = True
        print(f"Książka '{self.title}' została zwrócona.")


class Library:
    def __init__(self):
        self.books = []

 
    def add_book(self, book):
        self.book.append(book)
        print(f"Książka '{book.title}' została dodana do biblioteki.")

    

    def borrowed_book(self, title):
        for book in self.book:
            if book.tytul == title:
                book.returned()
                return
            print("Przepraszamy, nie ma takiej książki w bibliotece.")

    
    def returned_book(self, title):
        for book in self.book:
            if book.title == title:
               return
        print("Przepraszamy, nie ma takiej książki w bibliotece.")

todos = Book() 
todos = Library()