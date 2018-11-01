import subprocess

cat=subprocess.Popen(['python','pscat.py','passwd'],stdout=subprocess.PIPE)
tr=subprocess.Popen(['python','pstr.py'],stdin=cat.stdout,stdout=subprocess.PIPE)
nl=subprocess.Popen(['python','pscat.py'],stdin=tr.stdout,stdout=subprocess.PIPE)

for line in nl.communicate():
    if line:
        print(line.decode('ascii'))