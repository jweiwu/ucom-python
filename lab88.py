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
usersWillBeDeleted = session1.query(User).filter_by(name='user4')
for user in usersWillBeDeleted:
    session1.delete(user)
session1.commit()
session1.close()
