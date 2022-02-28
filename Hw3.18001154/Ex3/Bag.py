def balo(wt, val, W, n):
    result = [[-1 for i in range(W + 1)] for j in range(n + 1)]
    if n == 0 or W == 0:
        return 0
    if result[n][W] != -1:
        return result[n][W]

    if wt[n - 1] <= W:
        result[n][W] = max(
            val[n - 1] + balo(
                wt, val, W - wt[n - 1], n - 1),
            balo(wt, val, W, n - 1))
        return result[n][W]
    elif wt[n - 1] > W:
        result[n][W] = balo(wt, val, W, n - 1)
        return result[n][W]

val = [50,80 , 100]
wt = [5, 10, 15]
W = 50
n = len(val)
print(balo(wt, val, W, n))