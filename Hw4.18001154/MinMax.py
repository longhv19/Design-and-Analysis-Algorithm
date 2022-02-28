import numpy as np
import time
import matplotlib.pyplot as plt
import sys

INF = sys.maxsize
(min, max) = (INF, -INF)


def findMinMax(a, L, R, min, max):
    if L == R:
        if min > a[L]:
            min = a[L]
        if max < a[R]:
            max = a[R]
        return min, max
    if R - L == 1:
        if a[L] < a[R]:
            if min > a[L]:
                min = a[L]
            if max < a[R]:
                max = a[R]
        else:
            if min > a[R]:
                min = a[R]
            if max < a[L]:
                max = a[L]
        return min, max

    M = int((L + R) / 2)
    min, max = findMinMax(a, L, M, min, max)
    min, max = findMinMax(a, M + 1, R, min, max)
    return min, max

def array(n):
    return np.random.randint(100, size=n)

def runTime(n):
    start = time.time()
    a = array(n)
    findMinMax(a, 0, len(a)-1, min, max)
    return time.time() - start


n_length = [10,20,30,40,50,100,1000, 10000, 50000]
time_run = [runTime(i) for i in n_length]
print(time_run)
plt.scatter(n_length, time_run, s=20)
plt.title('Run Time')
plt.xlabel('Number')
plt.ylabel('Time')
plt.show()
