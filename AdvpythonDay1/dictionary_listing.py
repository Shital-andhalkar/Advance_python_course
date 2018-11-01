from os import listdir
from os.path import isdir,isfile,join,getmtime, getsize
from time import ctime

dir_path ="C:\\Users\\Sudhas4\\Downloads"

abs_path = join(dir_path, listdir(dir_path)[0])
print(abs_path)
print(isfile(abs_path))
print(isdir(abs_path))
print()
print(getsize(abs_path))
print(getmtime(abs_path))
print()
print(ctime(getmtime(abs_path)))