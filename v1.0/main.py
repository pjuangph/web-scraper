# multi-threaded function 
import threading 
from queue import Queue
from spider import Spider
from domain import *
from general import * 

PROJECT_NAME = 'thenewboston' # Kind of a constant
HOMEPAGE='https://ntrs.nasa.gov'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8

queue = Queue() # Thread queue
spider = Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)
print("done")

# Create worker threads (will die when main exits)
def create_workers(): 
    for x in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon=True # Dies when main exits
        t.start()

# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if (len(queued_links)>0): 
        print(str(len(queued_links) + " links left"))
        create_jobs()

# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.currentThread().name,url)
        queue.task_done() # tells os, ready for next job

create_workers()
crawl()