import time
import matplotlib.pyplot as plt
def binary(n):
    return bin(n).replace('0b', '')
def runTime(n):
    start = time.time()
    binary(n)
    runtime = time.time() - start
    return runtime
def drawthechart():
    array = [2,4,8,20,40,60]
    time = [runTime(i) for i in array]
    plt.scatter(array, time, s = 50)
    plt.title('Running time of binary')
    plt.xlabel('num')
    plt.ylabel('time')
    plt.show()
drawthechart()