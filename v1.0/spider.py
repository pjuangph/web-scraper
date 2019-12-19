"""
    Spider - Adds links to the waiting list
           - Gets the HTML
           - Adds page to crawled file
"""
import urllib.parse
from urllib.request import urlopen
from link_finder import LinkFinder
from general import *

class Spider:
    # Class variables (shared among all instances)
    project_name = '' 
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()


    def __init__(self,project_name,base_url,domain_name):
        # all spiders have this shared information
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider',Spider.base_url) # first spider crawls the base url
    
    @staticmethod    # this is a static method, dont need to pass self in
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name,Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file) # very first time it boots up, it gets an updated link and saves to set for faster operation
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' crawling ' + page_url)
            print("Queue " + str(len(Spider.queue)) + ' | Crawled')
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            print("Spider queue:" + str(len(Spider.queue)))
            Spider.queue.remove(page_url) # removed  the already cralwed file 
            Spider.crawled.add(page_url)
            Spider.update_files()
    @staticmethod
    def gather_links(page_url):
        """
            connects to the site, converts html to string
            parses the url, gather links

        """
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url,page_url)
            finder.feed(html_string)
        except ValueError as ex:
            print("Error: cannot crawl page")
            print(ex)
            return set()
        temp = set()
        temp.add(page_url)
        return temp.union(finder.page_links())
    
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            # Check if url is in waiting list
            # check if not in crawl list
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if (Spider.domain_name not in url): # if domain name is outside of the page, dont do anything
                continue
            Spider.queue.add(url)
    @staticmethod
    def update_files():
        set_to_file(Spider.queue,Spider.queue_file)
        set_to_file(Spider.crawled,Spider.crawled_file)

