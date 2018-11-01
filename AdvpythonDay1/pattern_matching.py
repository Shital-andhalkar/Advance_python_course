import re

s='the python and the perl'
pattern= 'p.+?n'

m=re.search(pattern, s, re.I)

if m:
    print('matc string: ',m.group())
    print(m.start())
    print(m.end())
    print(m.span())

    before=s[:m.start()]
    after = s[m.end():]
    print('before: {}|'.format(before))
    print('after: |{}'.format(after))

else:
    print('fail to match')

new='123.33.76.134'

newpattern = '(\d+)\.(\d+)\.(\d+)\.(\d+)'
n = re.search(newpattern,new,re.I)

if n:
    print('\n matching groups: ', n.group())
    print(n.group(1))
    print(n.group(4))