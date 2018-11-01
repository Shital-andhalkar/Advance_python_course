class Person:
    def __init__(self, fn, ln):
        self.fn=fn
        self.ln=ln
    def get_info(self):
        print('First-name:',self.fn)
        print('Last_name:', self.ln)

if __name__ == '__main__':
    p=Person('Shital','Andhalkar')
    p.get_info()