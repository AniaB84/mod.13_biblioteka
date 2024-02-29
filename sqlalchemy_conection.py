from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db', echo=True)

meta = MetaData()

library = Table(
   'library', meta,
   Column('id', Integer, primary_key=True),
   Column('title', String),
   Column('author', String),
)

meta.create_all(engine)
print(engine.table_names())