import threading
from shh_client import CustomSSHClient
import xml.etree.ElementTree as et
import logging
from time import sleep

logging.basicConfig(format='%(threadName)s : %(message)s')
target_file = 'sshresponse.log'

class ThreadedSSHHandler(CustomSSHClient):
    """thread function"""

    def __init__(self, host,port,user,pwd,job, lock):
        self.job=job
        self.lock=lock
        self.t_name=threading.current_thread().name
        super().__init__(host,port,user,pwd)
        self.__task_runner()

    def __task_runner(self):
        op=self.check_output(self.job)
        caption="{} ran {} @ {}".format(self.t_name, self.job, self.host)

        logging.warning('check for the lock')

        with self.lock:
            """critical section"""
            logging.warning('acquired the lock')

            with open(target_file,'a')as fw:
                fw.write(caption.center(80,'-')+"\n")
                fw.write(op)
                fw.write('\n')
                sleep(1)
            logging.warning('release the lock')

class ThreadedSSHClient:
    def __init__(self, hostfile):
        self.hosts=hostfile
        self.lock_obj=threading.Lock() #sync using lock
        self.__parse_host_file()

    def __parse_host_file(self):
        tree=et.parse(self.hosts)
        threads=[]

        for host_tag in tree.getiterator('host'):
            host_config=[]
            host_config.extend([host_tag.get('hostname'), int(host_tag.get('port'))])

            for child_tag in host_tag:
                host_config.append(child_tag.text)

            host_config.append(self.lock_obj)
            t=threading.Thread(target=ThreadedSSHHandler, args=host_config)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

if __name__ == '__main__':
    ThreadedSSHClient('../hosts.xml')

