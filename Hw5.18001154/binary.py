def print_binary(x):
    temp = ''
    for i in x:
        temp += str(i)
        # print(temp)
    return temp

def bin_gen(i):
    for j in range(0, 2):
        x[i] = j
        if i == (n-1):
            print(print_binary(x))
        else:
            bin_gen(i + 1)
n = 3
x = n*[0]
# print(x)
bin_gen(0)