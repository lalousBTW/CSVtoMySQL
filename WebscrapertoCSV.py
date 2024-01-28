from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


class WebscraperCSV:
    def __init__(self, url, page):
        self.url = url
        self.page = page
    
    def readpage(self):
        req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})   
        request_page = urlopen(req)
        page_html = request_page.read()
        self.page = page_html

        request_page.close()
    def findWhatIwant(self):
        self.readpage()
        html_soup = BeautifulSoup(self.page, 'html.parser')
        return html_soup
    
    def forloop(self,x =[],z =[], w = BeautifulSoup()):
        r = [] 
        for data in w.select(x[0], class_ = z[0]):
            if (len(x) == 1):
                r.append(data.get_text())
                return r
            del x[0]
            del z[0]
            self.forloop(x,z)
            
            
        


from bs4 import BeautifulSoup
x = BeautifulSoup();
url_to_scrape = WebscraperCSV("https://www.britannica.com/topic/list-of-countries-1993160", x)
print(url_to_scrape.findWhatIwant())
k = ['ul','a']
u = ['topic-list','md-crosslink']
print(url_to_scrape.forloop(k,u,url_to_scrape.findWhatIwant()))

