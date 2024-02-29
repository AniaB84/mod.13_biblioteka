from sqlalchemy import create_engine, MetaData, Integer, String, Table, Column

engine = create_engine('sqlite:///database.db', echo=True)

meta = MetaData()

library = Table(
   'library', meta,
   Column('id', Integer, primary_key=True),
   Column('title', String),
   Column('author', String),
)

conn = engine.connect()
s = library.select().where(library.c.id > 2)
result = conn.execute(s)

for row in result:
   print(row)
