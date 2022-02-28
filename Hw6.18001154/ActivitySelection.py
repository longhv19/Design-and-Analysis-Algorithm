def activity_selection(a, s, f, n):
    A = [0] * n
    A[1] = a[1]

    j = 1
    iter = 1

    for i in range(2, n + 1):
        if s[i] >= f[j]:
            iter += 1
            A[iter] = a[i]
            j = i

    A[0] = iter
    return A
#Danh sach cong viec
a = [0, 2, 3, 5, 1, 4]
#Thoi gian bat dau
s = [0, 0, 1, 3, 4, 1]
#Thoi gian ket thuc
f = [0, 2, 3, 4, 6, 6]

p = activity_selection(a, s, f, 5)

print('Lịch các công việc là: ')
for i in range(1, p[0] + 1):
    print(p[i])