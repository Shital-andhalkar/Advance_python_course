from os import listdir
from os.path import isdir,isfile,join,getmtime, getsize,basename
from time import ctime
from pprint import pprint as pp

class DictionaryListening:
    def __init__(self,*args):
        self.dictories = args
        self.container={}#dict()
        self.__read_dictionaries()

    def __read_dictionaries(self):
        try:
            for dir_name in self.dictories:
                list_of_abs_path=[join(dir_name,item) for item in listdir(dir_name)]

                for file_nm in filter(isfile,list_of_abs_path):
                    file_properties = [getsize(file_nm),ctime(getmtime(file_nm))]
                    file_nm = basename(file_nm)
                    self.container.setdefault(dir_name,{})[file_nm]=file_properties
        except FileNotFoundError as err:
            print(err)


if __name__ == '__main__':
    d1=DictionaryListening('C:\\Users\\Sudhas4\\Downloads')
    pp(d1.container)