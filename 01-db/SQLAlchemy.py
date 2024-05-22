import sqlalchemy as db
from sqlalchemy.orm import DeclarativeBase, Session

url = 'mariadb://root:1234@127.0.0.1:4200/test'
engine = db.create_engine(url, pool_size = 100)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __repr__(self):
        return f"id='{self.id}' \t name='{self.name}' \t email='{self.email}'"

def print_results ():
    result = db.select(User)

    for user in session.scalars(result):
        print(user)
    print ()

Base.metadata.drop_all(engine)

Base.metadata.create_all(engine)
session = Session(engine)

user1 = User(id = 1, name = 'Misha1', email = 'misha1@gmail.com')
user2 = User(id = 2, name = 'Misha2', email = 'misha2@outlook.com')
user3 = User(id = 3, name = 'Anaya', email = 'anaya@hotmail.com')
    
session.add_all([user1, user2, user3])
session.commit()

print ("Fetching all records: ")
print_results()

u = session.query(User).filter(User.name == "Anaya").first()
u.email = "anayanew@gmail.com"
session.commit()

print ("Fetching updated records: ")
print_results()

session.delete(u)
session.commit()

print ("Fetching records after deleting: ")
print_results()

session.close()