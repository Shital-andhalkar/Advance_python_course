"""demo for conditional variable"""

import threading
import logging
from time import sleep
from random import random

logging.basicConfig(format='%(threadName)s : %(message)s')

"""Producer-Consumer problem"""
def consume(cv, content):
    """Consumer thread function"""
    logging.warning('created and checking for the content..')
    with cv:
        if not content:
            logging.warning('waiting for the resource..')
            cv.wait()

    logging.warning('received the notification')
    logging.warning('consume.... {}'.format(content.pop(0)))



def produce(cv, content):
    """Producer thread function"""
    logging.warning('create')
    with cv:
        logging.warning('produces.. the resource..')
        for item in range(5):
            data = random()
            logging.warning('produced : {}'.format(data))
            content.append(data)

        cv.notify_all()

def main():
    """Main thread"""
    cond = threading.Condition()
    data_set = list()

    c1 = threading.Thread(target=consume, args=(cond, data_set), name='C1')
    c2 = threading.Thread(target=consume, args=(cond, data_set), name='C2')
    c1.start()
    c2.start()
    sleep(3)

    p = threading.Thread(target=produce, args=(cond, data_set), name='P')
    p.start()

if __name__ == '__main__':
    main()
