import threading
from time import sleep
from random import random

def worker(delay):
    """thread function"""

    t_name=threading.current_thread().getName()
    t_id=threading.current_thread().ident
    sleep(delay)
    print(t_name,':',t_id)

def main():
    """main thread"""
    list_of_threads =list()
    for item in range(1,6):
        rand_value=random()
        t=threading.Thread(target=worker,args=(rand_value,), name='t'+str(item))
        t.start()

    for t in list_of_threads:
        t.join()

    print('main thread is terminating')

if __name__ == '__main__':
    main()