import matplotlib.pyplot as plt
import time
import numpy as np
def selectionSort(array):
    for i in range(0, len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[j] < array[min]):
                min = j
        result = array[i]
        array[i] = array[min]
        array[min] = result
    return array

def createArray(n):
    return np.random.randint(100, size=n)

def runTime(n):
    start = time.time()
    selectionSort(createArray(n))
    runtime = time.time() - start
    return runtime

def drawthechart():
    n_size = [10, 10 ** 2, 10 ** 3]
    time = [runTime(i) for i in n_size]
    plt.scatter(n_size, time, s=100)
    plt.title("Time")
    plt.xlabel("Length")
    plt.ylabel("Time")
    plt.show()
drawthechart()



