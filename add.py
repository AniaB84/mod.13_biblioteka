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
   Create a new borrowed into the borrowed table
   :param conn:
   :param borrowed:
   :return: borrowed id
   """
   sql = '''INSERT INTO borrowed(library_id, tytuł, autor)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, borrowed)
   conn.commit()
   return cur.lastrowid


def add_returned(conn, returned):
   """
   Create a new returned into the returned table
   :param conn:
   :param returned:
   :return: returned id
   """
   sql = '''INSERT INTO returned(library_id, tytuł, autor)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, returned)
   conn.commit()
   return cur.lastrowid



if __name__ == "__main__":
   
   conn = create_connection("database.db")

  # Insert data from library.json into the database
   with open('library.json', 'r') as file:
        data = json.load(file)
        for item in data:
            library_id = add_library(conn, (item['title'], item['author']))
        
    
        with open('library.json', 'r') as file:
           data = json.load(file)
           for item in data:
               borrowed_id = add_borrowed(conn, (library_id, item['title'], item['author']))
            


        with open('library.json', 'r') as file:
            data = json.load(file)
            for item in data:
                returned_id = add_returned(conn, (library_id, item['title'], item['author']))

conn.commit()
   