import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)

# Create queue and crawled files
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt' # queue.txt is a list of links on the waiting list to be crawled
    crawled = project_name + '/crawled.txt'
    if not os.path.exists(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

# Create a new file
def write_file(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()

# Add data onto an existing file
def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data + '\n')

# Delete the contents
def delete_file_contents(path):
    with open(path,'w') as file:
        pass # do nothing

# read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results
# Iterate through a set, each item will be a line in the file
def set_to_file(links,file): # sets are a bunch of links
    delete_file_contents(file)
    for link in sorted(links): # go through links in order 
        append_to_file(file,link) # saves the set to file


