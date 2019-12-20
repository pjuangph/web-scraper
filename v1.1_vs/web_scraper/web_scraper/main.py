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