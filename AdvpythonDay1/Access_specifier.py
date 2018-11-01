class PackageManager:
    def __init__(self,name,version):
        self.__name=name
        self.version=version

    def __get_info(self):
        print('name:',self.__name)
        print('ver: ',self.version)

    def wrapper(self):
        self.__get_info()

if __name__ == '__main__':
    pm=PackageManager('pip','2.2.18')
    pm.wrapper()
    #print(pm.__name)
