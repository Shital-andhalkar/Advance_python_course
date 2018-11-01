import multiprocessing

def compute(rd,wt):
    data=rd.recv()
    wt.send(data.upper())

def main():
    rd1,wt1=multiprocessing.Pipe()
    rd2,wt2=multiprocessing.Pipe()

    child=multiprocessing.Process(target=compute , args=(rd1,wt2))
    child.start()

    content='ur mad'
    wt1.send(content)
    payload=rd2.recv()

    print('sent:',content)
    print('recv:',payload)

if __name__ == '__main__':
    main()