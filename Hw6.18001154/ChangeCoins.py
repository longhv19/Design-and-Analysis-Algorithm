def change_money(V):
    denomination = [1, 2, 5, 10, 20, 50, 100, 200, 500]

    n = len(denomination)

    answer = []

    i = n - 1
    while(i >= 0):
        while V >= denomination[i]:
            V = V - denomination[i]
            answer.append(denomination[i])
        i = i - 1

    for i in range(len(answer)):
        print(answer[i], end=' ')

n = 88
print('Change : ')
change_money(n)