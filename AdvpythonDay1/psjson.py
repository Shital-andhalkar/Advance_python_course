from psoserver import DictionaryListening

from json import dump

class DictionaryListing2json(DictionaryListening):
    def to_json(self,json_file):
        try:
            dump(self.container, open(json_file,'w'),indent=4)
        except(FileNotFoundError,IOError) as err:
            print(err)
if __name__ == '__main__':
    DictionaryListing2json('C:\\Users\\Sudhas4\\Downloads','C:\\Users').to_json('tmp.json')