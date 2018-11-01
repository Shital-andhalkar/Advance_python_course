import requests
import multiprocessing
from requests.exceptions import ConnectionError


def web_crawler(q):
    """"""
    try:
        p_name=multiprocessing.current_process().name
        url = q.get()
        payload=requests.get(url).content
        print("{}:{}:{}".format(p_name,url,payload[:128]))
    except ConnectionError as err:
        print(err)

def main():

    """parent process"""
    queue_obj= multiprocessing.Queue()
    urls=['http://python.org','http://linux.org', 'http://kernel.org/', 'http://google.com']

    for url in urls:
        child=multiprocessing.Process(target=web_crawler,args=(queue_obj,))
        child.start()

    for url in urls:
        queue_obj.put(url)#add urls in to queue


if __name__ == '__main__':
    main()
