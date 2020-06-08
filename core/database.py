import os, sys
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))
from core.models import Post, Urllib, session

def insert_post(title,body,original_link):
    newpost = Post(title=title, content=body, original_link=original_link )
    session.add(newpost)
    session.commit()  

def delete_all_post():
    selected = session.query(Post).all()
    for i in selected:
        session.delete(i)
    session.commit()
def view_all_post():
    selected = session.query(Post).all()
    return selected
def receive_lib(website_url):
    received = session.query(Urllib).filter_by(website_url=website_url).first()
    return received
def import_lib(name, url, title_tag, body_tag):
    newlib = Urllib(website_name=name, website_url=url, website_title_tag=title_tag, website_body_tag=body_tag)
    session.add(newlib)
    session.commit()