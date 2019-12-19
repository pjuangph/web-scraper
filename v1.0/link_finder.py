from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser): # Inherits from html parser
    def __init__(self,base_url,page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self,tag,attrs):
        if tag == 'a': # link tag
            for (attribute,value) in attrs:
                if (attribute=='href'):
                    # Convert to full URL
                    url = parse.urljoin(self.base_url,value) # if it already is the full url then it keeps and formats properly
                    self.links.add(url)
    
    
    def page_links(self):
        return self.links

    def error(self,message):
        pass



