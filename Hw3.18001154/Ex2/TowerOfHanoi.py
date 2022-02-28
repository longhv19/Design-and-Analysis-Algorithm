import time
import matplotlib.pyplot as plt
start = time.time()
def towers_of_Hanoi(n,o,d,a):
    if n == 1:
        print('Move disk',n,'from rod',o,'to rod',d)
    else:
        towers_of_Hanoi(n-1,o,a,d)
        print('Move disk',n,'from rod',o,'to rod',d)
        towers_of_Hanoi(n-1,a,d,o)
def towers_of_Hanoi_alt(n,o,d,a):
    if n > 0:
        towers_of_Hanoi_alt(n-1,o,a,d)
        print('Move disk',n,'from rod',o,'to rod',d)
        towers_of_Hanoi_alt(n-1,a,d,o)
towers_of_Hanoi(4, 'O','D','A')



runtime = time.time()-start

print('Running time : ', runtime)
# def drawthechart():
#     n_length = [10,20,30,40,50]
#     time = [calTime(i) for i in n_length]
#     plt.scatter(n-n_length, time, s = 50)
#     plt.title("Run Time")
#     plt.xlabel('Number')
#     plt.ylabel('Time')
#     plt.show()