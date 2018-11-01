import paramiko

class CustomSSHClient:
    def __init__(self,host,port ,user ,pwd):
        self.host = host
        self.user = user
        self.port = port
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.user, pwd)

    def upload(self, filename):
        """sftp upload"""
        print ('uploading ', filename)
        sftp = self.ssh.open_sftp()
        sftp.put(filename, '/root/'+filename)
        print ('uploaded ', filename)
        sftp.close()

    def check_output(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        return stdout.read(), stderr.read()


    def __del__(self):
        self.ssh.close()

if __name__ == '__main__':
    ssh = CustomSSHClient('10.199.196.125',22 ,'root','abc123')
    op, op2 = ssh.check_output('ls')
    print(op)