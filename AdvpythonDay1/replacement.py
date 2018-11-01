import re

s= 'root:x:0:0:root:/root:/bin/bash'
pattern=':'
repalcement=','

s2= re.sub(pattern,repalcement, s)
print(s2)
print()
s3=re.sub('[AEIOU]','*',s2, flags=re.I)
print(s3)