import math

def closest_pair(s):
    def sort(s):
        return [u for (u,i) in sorted(enumerate(s), key= lambda p: p[1])]

    a = sort(s)

    def distance(i,j):
        return abs(s[i] - s[j])

    def search(i,j):
        if i >= j:
            return None
        elif i + 1 == j:
            return (a[i], a[j])
        else:
            k = (i + j) // 2
            left = search(i, k)
            right = search(k, j)
            (i_left, j_left) = left
            (i_right, j_right) = right

            if left is None:
                (i_min, j_min) = right
            elif right is None:
                (i_min, j_min) = left
            else:
                d_left = distance(i_left, j_left)
                d_right = distance(i_right, j_right)
                if d_left < d_right:
                    (i_min, j_min) = left
                else:
                    (i_min, j_min) = right
            return  (i_min, j_min)
    return search(0, len(s) - 1)

print(closest_pair([8,4,7,10,14]))
print(closest_pair([1,20,45,33,67,88,55,100,999,1000,2,450]))
