from .sqlalchemy_conection import library, engine

ins = library.insert()

ins = library.insert().values(title='Opowiesci z Narnii Srebrne Krzeslo', author='C.S. Lewis')

conn = engine.connect()
result = conn.execute(ins)
conn.execute(ins, [
   {'title': 'Opowiesci z Narnii Kon i jego chlopiec', 'author': 'C.S. Lewis'},
   {'title': 'Opowiesci z Narnii Siosrzeniec Czarodzieja', 'author': 'C.S. Lewis'},
])