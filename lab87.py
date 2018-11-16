from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lab86 import User, Base

# engine = create_engine('sqlite:///.//data//lab87.sqlite', echo=True)
engine = create_engine('mysql+mysqlconnector://pythondemo:pythondemo@localhost:3306/pythondemo',
                       echo=True, pool_recycle=3600)
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

session3 = Session()
userShouldBeChanged = session3.query(User).filter_by(name='user1').first()
print [session3.dirty]
userShouldBeChanged.fullname = "USER THAT HAD BEEN CHANGED"
print [session3.dirty]
user4 = User(name='user4', fullname="the Fourth User", password='xyz')
print [session3.new]
session3.add_all([user4])
print [session3.new]
session3.commit()
session1.close()
session2.close()
session3.close()
