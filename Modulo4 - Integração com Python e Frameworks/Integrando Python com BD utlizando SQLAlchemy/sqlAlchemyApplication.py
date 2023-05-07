from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import func
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import select

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    # declarator attributes
    id = Column(Integer, primary_key=True)
    name = Column(String)
    full_name = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f'User account = id:{self.id}, name:{self.name}, fullname:{self.full_name}'



class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)  # nullable=False, é nao deixar o campo aceitar nulo
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f'Address  = id:{self.id}, email_address:{self.email_address}'


print(User.__tablename__)
print(Address.__tablename__)

# criando conexão com banco de dados

engine = create_engine('sqlite://')

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# inspecionar tabelas
inspetor_engine = inspect(engine)
print(inspetor_engine.has_table('address'))

print(inspetor_engine.get_table_names())

with Session(engine) as session:
    gustavo = User(
        name='gustavo',
        full_name='gustavo franco',
        address=[Address(email_address='gustavof@dio.me')]
    )
    gustavo2 = User(
        name='gustavo',
        full_name='gustavo osorio franco',
        address=[Address(email_address='gustavof@dio.me')]
    )
    luanna = User(
        name='luanna',
        full_name='luanna franco',
        address=[Address(email_address='luannaaf@dio.me'),
                 Address(email_address='luanna123@teste.com')]
    )
# enviar para o db(persistir dados)
# session.add_all(session)
# outra maneira de enviar para o db
session.add_all([gustavo,luanna, gustavo2, gustavo])

session.commit()

# recuperar dados do db
statement = select(User)
for user in session.scalars(statement):
    print(user)
print('\n')

statement = select(User).where(User.name.in_(['gustavo', 'luanna', 'luan']))
for user in session.scalars(statement):
    print(user)
print('\n')

# Recuperando usuário que tem mais de um endereço de email, passado a posição em que está
statement_address = select(Address).where(Address.user_id.in_([2]))
for address in session.scalars(statement_address):
    print(address)
print('\n')

# order by
ordem = select(User).order_by(User.full_name.desc())
for user in session.scalars(ordem):
    print(user)
print('\n')
# inner join
join_statement = select(User.full_name, User.name, User.id, Address.email_address).join_from(Address, User)
for user in session.scalars(join_statement):
    print(user.title())
print('\n')

# criando conexão para ordernar dados em vez de utilizar a session
connection = engine.connect()
results = connection.execute(join_statement)
for result in results:
    print(result)
print('\n')

statement_count = select(func.count('*')).select_from(User)
print(statement_count)
for user in session.scalars(statement_count):
    print(user)
