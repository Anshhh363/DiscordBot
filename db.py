from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    MetaData,
    Table,
    BigInteger,
)

from sqlalchemy.ext.declarative import declarative_base

"""this is the db part wherein all the db processes and table exists"""
engine = create_engine("mysql+mysqldb://root:tigertiger@localhost/botServer", echo=True)

"""metaData is used in order to create a table in the database if already it doesn't exist"""

metadataObj = MetaData()

Base = declarative_base()

ServerAuths = Table(
    "ServerAuths",
    metadataObj,
    Column("id", BigInteger, primary_key=True, autoincrement=False),
    Column("ServerName", String(50), nullable=False),
)

metadataObj.create_all(engine)


class ServerAuths(Base):
    __tablename__ = "ServerAuths"

    id = Column(BigInteger, primary_key=True, autoincrement=False)
    ServerName = Column(String, nullable=False)
