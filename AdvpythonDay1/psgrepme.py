import re
from fileinput import input, filename, filelineno
from psarchive import glob
class Grepme:
    def __init__(self, pattern, *args):
        self.pattern=pattern
        self.filename=args
        self.__do_match()

    def __do_match(self):
        for line in input(self.filename):
            if re.search(self.pattern,line, re.I):
                print('{}:{}:{}'.format(filename(),filelineno(),line), end='')

if __name__ == '__main__':
    Grepme('import', *glob('*.py'))

for line in input('passwd.txt', inplace=True, backup='.bak'):
    if filelineno()<=10:
        line = re.sub(':', ',', line)
    print(line, end='')