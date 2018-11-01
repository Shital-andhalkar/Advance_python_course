import threading
from shh_client import CustomSSHClient
import xml.etree.ElementTree as et

target_file = 'sshresponse.log'

class ThreadedSSHHandler(CustomSSHClient):
    """thread function"""

    def __init__(self, host,port,user,pwd,job):
        self.job=job
        self.t_name=threading.current_thread().name
        super().__init__(host,port,user,pwd)
        self.__task_runner()

    def __task_runner(self):
        op=self.check_output(self.job)
        caption="{} ran {} @ {}".format(self.t_name, self.job, self.host)

        with open(target_file,'a')as fw:
            """critical section"""
            fw.write(caption.center(80,'-')+"\n")
            fw.write(op)
            fw.write('\n')

class ThreadedSSHClient:
    def __init__(self, hostfile):
        self.hosts=hostfile
        self.__parse_host_file()

    def __parse_host_file(self):
        tree=et.parse(self.hosts)
        threads=[]

        for host_tag in tree.getiterator('host'):
            host_config=[]
            host_config.extend([host_tag.get('hostname'), int(host_tag.get('port'))])

            for child_tag in host_tag:
                host_config.append(child_tag.text)

            t=threading.Thread(target=ThreadedSSHHandler, args=host_config)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

if __name__ == '__main__':
    ThreadedSSHClient('../hosts.xml')

