import sqlite3
import json

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except sqlite3.Error as e:
       print(e)
   return conn

def add_library(conn, library):
   """
   Create a new library into the projects table
   :param conn:
   :param library:
   :return: library id
   """
   sql = '''INSERT INTO library(tytuł, autor)
             VALUES(?,?)'''
   cur = conn.cursor()
   cur.execute(sql, library)
   conn.commit()
   return cur.lastrowid

def add_borrowed(conn, borrowed):
   """
   Create a new task into the borrowed table
   :param conn:
   :param borrowed:
   :return: borrowed id
   """
   sql = '''INSERT INTO borrowed(library_id, tytuł, autor, date)
             VALUES(?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, borrowed)
   conn.commit()
   return cur.lastrowid

if __name__ == "__main__":
  
   conn = create_connection("database.db")

   # Insert data from library.json into the database
   with open('todos.json', 'r') as file:
       reader = json.reader(file)
       next(reader)  # Skip header
       for row in reader:
           library = (row[0], row[1])
           library_id = add_library(conn, library)       
           ly_id = add_library(conn, library)
  
   # Insert data from borrowed into the database
   with open('todos.json', 'r') as file:
       reader = json.reader(file)
       next(reader)  # Skip header
       for row in reader:
           borrowed = (library_id, row[0], row[1], row[2])
           borrowed_id = add_borrowed(conn, borrowed)
   

   br_id = add_borrowed(conn, borrowed)

   print(ly_id, br_id)
   conn.commit()
   