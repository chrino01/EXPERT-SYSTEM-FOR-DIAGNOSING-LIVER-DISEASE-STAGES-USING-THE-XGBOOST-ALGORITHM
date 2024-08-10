from sqlalchemy import create_engine,text,Integer,VARCHAR,String,Float,BLOB,PickleType,ForeignKey,Text
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship


engine = create_engine('mysql://chrinoplus@localhost/chrinoplus')

with engine.connect() as connection:
    result = connection.execute(text('select "Hello"'))

    print(result.all())
