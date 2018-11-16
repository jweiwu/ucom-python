from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lab86 import User, Base

engine = create_engine('sqlite:///:memory:', echo=True)
print "get a user table:", User.__tablename__, User.__table__

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session1 = Session()
user1 = User(name='user1', fullname='first user', password='user1pwd')
user2 = User(name='user2', fullname='second user', password='user2pwd')
session1.add(user1)
session1.add(user2)
session1.commit()
session2 = Session()
for u in session2.query(User):
    print "[*]user inside is:", u
session2.commit()
