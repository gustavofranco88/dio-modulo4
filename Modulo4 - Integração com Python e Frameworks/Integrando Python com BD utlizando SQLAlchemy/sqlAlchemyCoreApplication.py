from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import text

engine = create_engine('sqlite:///:memory:')

metadata_obj = MetaData()  # pode definir sem o schema.
user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False)
)
user_prefs = Table(
    'user_prefs',
    metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.user_id'), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(160)),
)
metadata_obj.create_all(engine)
conn = engine.connect()
result = conn.execute(text('select * from user'))
print('ANTES DA INSERÇÃO')
for row in result:
    print('row')

print('inserindo dados no banco')
conn.execute(text("insert INTO user values(1,'Gustavo', 'g@gmailcom', 'gfranco')"))
conn.execute(text("insert INTO user values(2,'Gustavo', 'g@gmailcom', 'gfranco')"))
conn.execute(text("insert INTO user values(3,'Gustavo', 'g@gmailcom', 'gfranco')"))
conn.execute(text("insert INTO user values(4,'Gustavo', 'g@gmailcom', 'gfranco')"))
conn.execute(text("insert INTO user values(5,'Gustavo', 'g@gmailcom', 'gfranco')"))
conn.execute(text("insert INTO user values(6,'Gustavo', 'g@gmailcom', 'gfranco')"))

print('deletando dados do banco')
conn.execute(text('delete from user where user_id==2'))


result2 = conn.execute(text('select * from user'))
print('DEPOIS DA INSERÇÃO')
for row in result2:
    print(row)


for table in metadata_obj.sorted_tables:
    print(table)


'''
print('\nPreferencia de Usuários\n')
print(user_prefs.primary_key)
print(user.primary_key)

#result = connection.execute('select * from user')
# result.execute(sql)
# Execute uma consulta SQL para criar uma tabela
#engine.connect()
# connection.execute('select * from user')
'''