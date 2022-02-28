import numpy as np
import time
import matplotlib.pyplot as plt

def binarySearch(a,x,L,R):
    if(L > R):
        return -1
    M = int((L+R) / 2)
    if(x == a[M]):
        return M
    if(x < a[M]):
        return binarySearch(a,x,L,M-1)
    else:
        return binarySearch(a, x, M+1, R)

def array(n):
    temp = np.sort(np.random.randint(100, size=n))
    return temp

def runTime(n):
    start = time.time()
    a = array(n)
    binarySearch(a, 0, len(a)-1, 10)
    timerun = time.time()-start
    return timerun

def drawthechart():
    n = [10,20,50,100,1000, 10000]
    time = [runTime(i) for i in n]
    print(time)

    plt.scatter(n, time, s=50)
    plt.xlabel("Number")
    plt.ylabel('Time')
    plt.show()
drawthechart()

