#tc: tổng chi phí khi đi
#Độ phức tạp: O(nm)
import time

start = time.time()
row = 3
col = 3

def path_in_numeric_table(cost, m, n):
    #khởi tạo bảng chi phí
    tc = [[0 for i in range(col)] for i in range(row)]

    tc[0][0] = cost[0][0]

    #Khởi tạo cột đầu tiên của bảng tổng đường đi
    for i in range(1, m + 1):
        tc[i][0] = tc[i - 1][0] + cost[i][0]

    #khởi tạo hàng đầu tiên của bảng tổng đường đi
    for j in range(1, n + 1):
        tc[0][j] = tc[0][j - 1] + cost[0][j]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tc[i][j] = max(tc[i-1][j-1],
                           tc[i-1][j],
                           tc[i][j - 1] + cost[i][j])
    return tc[m][n]
cost = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
print('Tổng giá trị lớn nhất các ô')
print(path_in_numeric_table(cost, 2, 2))
runtime = time.time() - start
print('Time Running : ', runtime)


