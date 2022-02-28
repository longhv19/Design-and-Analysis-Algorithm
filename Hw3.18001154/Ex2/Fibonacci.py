import time
import numpy as np
import matplotlib.pyplot as plt
# start = time.time()
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(35))
# runtime = time.time() - start
# print(runtime)
def createNum(n):
    return np.random.randint(50)
def runtime(n):
    start = time.time()
    fibonacci(createNum(n))
    run = time.time() - start
    return run

def drawthechart():
    n_sie = [10, 20, 30, 35]
    time = [runtime(i) for i in n_sie]
    plt.scatter(n_sie, time, s=100)
    plt.title("Time")
    plt.xlabel("Number")
    plt.ylabel('Time')
    plt.show()
drawthechart()