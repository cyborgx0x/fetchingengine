
# import mysql.connector
# config = {
#   'user': 'bb7rscqll4s4fucu',
#   'password': 'o4q5vdaua9r1k7x3',
#   'host': 'un0jueuv2mam78uv.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
#   'database': 'wp0cqq4t5leuhx3v',
#   'raise_on_warnings': True
# }
# def printallpost():
#     cnx = mysql.connector.connect(**config)
#     cursor = cnx.cursor()
#     query = ("SELECT * FROM post ")
#     cursor.execute(query)
#     for i in cursor:
#         print(i)
#     cursor.close()
#     cnx.close()

# from sqlalchemy import MetaData, Integer, Unicode, String, create_engine, Column, DateTime
# from datetime import datetime
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()
# meta = MetaData()
# engine = create_engine('mysql://bb7rscqll4s4fucu:o4q5vdaua9r1k7x3@un0jueuv2mam78uv.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/wp0cqq4t5leuhx3v')

# class Post(Base):
#     'posts', meta
#     __tablename__ = 'post'
#     id = Column('id',Integer, primary_key=True)
#     title = Column('post_title',Unicode(300))
#     content = Column('post_content',Unicode(5000))
#     timestamp = Column('post_date_gmt',DateTime, index=True, default=datetime.now)
#     excerpt = Column('post_excerpt',Unicode(200))
#     original_link = Column('original_link', Unicode(300))
    

#     def __repr__(self):
#         return 'Post {}>'.format(self.content)
    
# class User(Base):
#     'users', meta
#     __tablename__ = 'user'
#     id = Column('id', Integer, primary_key=True)
#     first_name = Column('first_name',Unicode(50))
#     last_name = Column('last_name',Unicode(50))
#     user_name = Column('user_name', String(20))
#     email = Column('email', String(64))
#     password_hash = Column(String(128))
