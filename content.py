from core.engine import parse_url, Website, Content
from core.database import receive_lib
from bs4 import BeautifulSoup
import lxml
import re
import requests

def get_url(link):
    chapter_list_source = requests.get(link).text
    r = BeautifulSoup(chapter_list_source, 'lxml')
    chapter_list = r.select(comparing)
    # urls = [e.a.attrs['href'] for e in chapter_list]
    return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(chapter_list))

link='https://truyenfull.vn/cau-ma/'
coreurl=link.split('/')[2]
urllibrary={
"truyenfull.vn":"div#list-chapter",
"truyen.tangthuvien.vn":"ul.cf"
}
comparing=urllibrary[coreurl]

lib = receive_lib(coreurl)
site = Website(lib.website_name, lib.website_url, lib.website_title_tag, lib.website_body_tag)

def get_fictions(link):
    links = get_url(link)
    for l in links:
        parse_url(site, l)
        
get_fictions(link)