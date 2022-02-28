#1: la vat can trong ma tran ban dau
#0: la nhung vi tri co the di
maze = [[0,1,0,1,1],
        [0,0,0,0,0],
        [1,0,1,0,1],
        [0,0,1,0,0],
        [1,0,0,1,0]]

# maze = [ [1, 0, 0, 0],
#          [1, 1, 0, 1],
#          [0, 1, 0, 0],
#          [1, 1, 1, 1] ]

# SIZE = 4
SIZE = 5
solution = [[0]*SIZE for _ in range(SIZE)]

def solvemaze(r, c):
    if (r == SIZE-1) and (c == SIZE-1):
        solution[r][c] = 1
        return True

    if r>=0 and c>=0 and r<SIZE and c<SIZE and solution[r][c] == 0 and maze[r][c] == 0:
        solution[r][c] = 1

        if solvemaze(r + 1, c):
            return True
        if solvemaze(r, c + 1):
            return True
        if solvemaze(r - 1, c):
            return True
        if solvemaze(r, c - 1):
            return True
        solution[r][c] = 0
        return False
    return 0
if(solvemaze(0,0)):
    for i in solution:
        print(i)
else:
    print('No solution!')
#1: la duong di tim thay trong ma tran in ra
