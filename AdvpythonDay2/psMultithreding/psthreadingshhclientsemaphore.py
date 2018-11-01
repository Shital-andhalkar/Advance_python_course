import threading
from shh_client import CustomSSHClient
import xml.etree.ElementTree as et
import logging
from time import sleep

logging.basicConfig(format='%(threadName)s : %(message)s')
target_file = 'sshresponse.log'

class ThreadedSSHHandler(CustomSSHClient):
    """thread function"""
    def enroll(self,t_name):
        self.pool.append(t_name)

    def remove(self,t_name):
        self.pool.remove(t_name)

    def __init__(self, host,port,user,pwd,job, sema, pool, lock):
        self.job=job
        self.semaphore=sema
        self.pool=pool
        self.lock=lock
        self.t_name=threading.current_thread().name
        super().__init__(host,port,user,pwd)
        self.__task_runner()

    def __task_runner(self):
        op=self.check_output(self.job)
        caption="{} ran {} @ {}".format(self.t_name, self.job, self.host)

        logging.warning(self.pool)

        with self.semaphore:
            """critical section for semaphore"""
            self.enroll(self.t_name)
            logging.warning('enrolled' +str(self.pool))

            with self.lock:
                with open(target_file,'a')as fw:
                    fw.write(caption.center(80,'-')+"\n")
                    fw.write(op)
                    fw.write('\n')
                    sleep(1)
                logging.warning('done with critical section')
            self.remove(self.t_name)
            logging.warning("exits: {}".format(self.pool))

class ThreadedSSHClient:
    """main thread"""
    def __init__(self, hostfile):
        self.hosts=hostfile
        self.sema_obj=threading.Semaphore(2) #sync using lock
        self.lock_obj=threading.Lock()
        self.sema_pool=[]
        self.__parse_host_file()

    def __parse_host_file(self):
        tree=et.parse(self.hosts)
        threads=[]

        for host_tag in tree.getiterator('host'):
            host_config=[]
            host_config.extend([host_tag.get('hostname'), int(host_tag.get('port'))])

            for child_tag in host_tag:
                host_config.append(child_tag.text)

            host_config.extend([self.sema_obj,self.sema_pool,self.lock_obj])
            t=threading.Thread(target=ThreadedSSHHandler, args=host_config)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()


if __name__ == '__main__':
    ThreadedSSHClient('../hosts.xml')

