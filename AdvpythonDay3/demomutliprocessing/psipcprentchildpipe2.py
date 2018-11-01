import multiprocessing
from subprocess import check_output

def compute(rd,wt):
    data=rd.recv()
    wt.send(check_output(data).decode('ascii'))

def main():
    rd1,wt1=multiprocessing.Pipe()
    rd2,wt2=multiprocessing.Pipe()

    child=multiprocessing.Process(target=compute , args=(rd1,wt2))
    child.start()

    content=['ipconfig']
    wt1.send(content)
    payload=rd2.recv()

    print('sent:',content)
    print('recv:',payload)

if __name__ == '__main__':
    main()