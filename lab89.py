from sqlalchemy import Table, MetaData, Column, Integer, create_engine
from sqlalchemy.types import String

engine = create_engine('mysql+mysqlconnector://pythondemo:pythondemo@localhost:3306/pythondemo',
                       echo=True, pool_recycle=3600)
metadata = MetaData()
t = Table('DEMOSALES', metadata,
          Column('ID', Integer, primary_key=True),
          Column('PRODUCT', String(100)),
          Column('COUNT', Integer))
metadata.create_all(engine)

for table in metadata.sorted_tables:
    print table.name
