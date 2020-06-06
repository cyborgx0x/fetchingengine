from core.engine import  Website, Crawler

class News:
    """
    class for the job that we get
    """
    def __init__(self,url,title, excerpt):
        self.url = url
        self.title = title
        self.excerpt = excerpt
    def __repr__(self):
        return '{}  \n {}  \n {}'.format(self.url,self.title,self.excerpt)

    
class Newsparser(Crawler):
    def parse(self, site, url):
        file = self.getpage(url)
        if file is not None:
            title = self.selector(file, site.titletag)
            excerpt = self.selector(file, site.bodytag)
            if title != '' and excerpt != '':
                news = News(url, title, excerpt)
            print(news)


                

def get_news(link):
    crawler = Newsparser()
    urllib =[['dantri','dantri.com.vn','title', 'div.dt-news__sapo']]
    websites=[]
    for row in urllib:
        websites.append(Website(row[0], row[1], row[2], row[3]))
    crawler.parse(websites[0],link)   
