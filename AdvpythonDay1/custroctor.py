class  SystenInfo:
        def __init__(self):
            print(self,'am in constructor')
        def __del__(self):
            print(self,'deleted')
if __name__ == '__main__':
        si=SystenInfo()
        print(si)
