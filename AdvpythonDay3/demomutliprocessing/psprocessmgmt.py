import subprocess
from os import getpid

print("parent process id: ",getpid())

op=subprocess.check_output(['bash','-c','echo$$'])
print('child_process: ',op)

status=subprocess.call(['cal'])
print("exit status:",status)