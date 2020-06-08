from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, Unicode, String, DateTime, Column, Text
from datetime import datetime
from sqlalchemy import MetaData
import os
basedir = os.path.abspath(os.path.dirname(__file__))
Base = declarative_base()

engine = create_engine('mysql://root:123456@localhost:3306/max?charset=utf8mb4', echo =True)
Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()
meta = MetaData()

class Post(Base):
    'engine', meta
    __tablename__ = 'engine'
    id = Column('id',Integer, primary_key=True)
    title = Column('post_title',Unicode(300))
    content = Column('post_content',Text)
    timestamp = Column('post_date_gmt',DateTime, index=True, default=datetime.now)
    excerpt = Column('post_excerpt',Unicode(200))
    original_link = Column('original_link', Unicode(300))
    
    def __repr__(self):
        return '<Post(title={}, content={}, timestamp={}, excerpt={}, original_link={})>'.format(self.title,self.content,self.timestamp,self.excerpt,self.original_link)
        
class User(Base):
    'users', meta
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name',Unicode(50))
    last_name = Column('last_name',Unicode(50))
    user_name = Column('user_name', String(50))
    email = Column('email', String(64))
    password_hash = Column(String(128))

class Urllib(Base):
    'urllib', meta
    __tablename__ = 'url_lib'
    id = Column('id', Integer, primary_key=True)
    website_name = Column('website_name', String(100))
    website_url = Column('website_url', String(100))
    website_title_tag = Column('website_title_tag', String(100))
    website_body_tag = Column('website_body_tag', String(100))
