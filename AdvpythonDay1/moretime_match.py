import re

s='the python and the perl scripting'
pattern= 'p.+?n'

for m in re.finditer(pattern,s,re.I):
    print(m.group())
    print(m.span())

print(re.findall(pattern,s,re.I))