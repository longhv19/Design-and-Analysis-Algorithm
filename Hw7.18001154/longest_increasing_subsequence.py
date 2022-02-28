# s là dãy con
# m là mảng để lưu kết quả đếm các dãy con
import time

start = time.time()
def list(i, s, m):
    if m[i] != -1:
        return m[i]
    else:
        max_len = 1
        for j in range(i + 1, len(s)):
            if s[j] > s[i]:
                temp = list(j, s, m) + 1
                # print(temp)
                if max_len < temp:
                    max_len = temp
        m[i] = max_len
        # print(m[i])
        return max_len

def longest_increasing_subsequence(s):
    m = [-1]*len(s)
    m[len(s) - 1] = 1
    for i in range(len(s)):
        list(i, s, m)

    print('Longest increasing subsequence : ' + str(max(m)))
    # print(m)
    return max(m)

timerun = time.time() - start
seq1 = [2, 5, 4, 6, 3, 8, 9, 7]
seq2 = [11, 17, 5, 8, 6, 4, 7, 12, 3]

longest_increasing_subsequence(seq1)
print('Time running : ', timerun)