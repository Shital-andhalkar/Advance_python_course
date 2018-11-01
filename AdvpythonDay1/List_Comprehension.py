from timeit import timeit

def demo1():
    items=[1,3,5,6,7,3,8]
    temp =[]
    for i in items:
        temp.append(bin(i))
    return temp

def demo2():
    items=[1,3,5,6,7,3,8]
    temp2=[bin(i) for i in items] #list comprehension
    return temp2
if __name__ == '__main__':

    print(timeit('demo1()',setup='from __main__ import demo1', number=100000))
    print(timeit('demo2()',setup='from __main__ import demo2', number=100000))