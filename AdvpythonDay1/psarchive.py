"""abstract class and method"""
from abc import ABC, abstractmethod
from zipfile import ZipFile
from glob import glob

class ArchiveManager(ABC):
    """abstract class"""
    @abstractmethod # decorative
    def save(self):
        """abstract method"""
        pass

class ZIPArchive(ArchiveManager):
    """concrete class"""

    def __init__(self,name):
        self.archive_name=name

    def save(self, *args):
        with ZipFile(self.archive_name,mode='w')as zf: #context manager
            for file_name in args:
                zf.write(file_name)
                print('added : ',file_name)


class TarArchive(ArchiveManager):
    pass


class Unsupported_archive_exception(Exception):
    def __str__(self):#custome exception
        return '{}: {}'.format(self.__class__.__name__, self.args[0])

def make_archive(archive_name, archive_type='zip'):
    """factory method"""
    archive = None

    if archive_type=='zip':
        archive=ZIPArchive(archive_name)
    elif archive_type =='tar':
        archive=TarArchive(archive_name)
    else:
        raise Unsupported_archive_exception('unsupported archive format :{}'.format(archive_type))

    return archive

if __name__ == '__main__':
    make_archive('src.zip').save(*glob('*.py'))
