from fileinput import input,filelineno

for line in input():
    print("{:>6} {}".format(filelineno(), line), end='')
