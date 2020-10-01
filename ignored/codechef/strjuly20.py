try:
    import numpy
    from functools import reduce
    n = int(input())
    for i in range(0,n,1):
        plucks = int(input())
        net = list(map(int, input().split()))
        arr=net[:]
        arr.pop()
        net.pop(0)
        net = numpy.subtract(net,arr)
        total = reduce((lambda x,y:x+y), net)
        print(total-plucks+1)
except:
    pass

