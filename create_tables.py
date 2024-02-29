import sqlite3
from sqlite3 import Error

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
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

if __name__ == "__main__":

   create_library_sql = """
   -- library table
   CREATE TABLE IF NOT EXISTS library (
      id integer PRIMARY KEY,
      tytuł text,
      autor text
   );
   """

   create_borrowed_sql = """
   -- zadanie table
   CREATE TABLE IF NOT EXISTS borrowed (
      id integer PRIMARY KEY,
      library_id integer NOT NULL,
      tytuł text,
      autor text,
      FOREIGN KEY (library_id) REFERENCES library (id)
   );
   """

   create_returned_sql = """
   -- zadanie table
   CREATE TABLE IF NOT EXISTS returned (
      id integer PRIMARY KEY,
      library_id integer NOT NULL,
      tytuł text,
      autor text,
      FOREIGN KEY (library_id) REFERENCES library (id)
   );
   """

   db_file = "database.db"

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_library_sql)
       execute_sql(conn, create_borrowed_sql)
       execute_sql(conn, create_returned_sql)
       
