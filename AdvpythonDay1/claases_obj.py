import os

class  SystenInfo:
    pass
if __name__ == '__main__': #name space validation ......entry point
    si=SystenInfo()
    print(si)
    print(SystenInfo)
    print(__name__)#default namespace in python
    print(os.__name__)