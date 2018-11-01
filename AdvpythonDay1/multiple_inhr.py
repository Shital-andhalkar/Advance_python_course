"""Multiple inheritance"""

class Alpha :
    def pprint(self):
        print('alpha')


class beta:
    def pprint(self):
        print('beta')

class Shital(Alpha,beta):
    def pprint(self):
        super().pprint()
        Alpha().pprint()
        beta().pprint()
if __name__ == '__main__':
    Shital().pprint()
