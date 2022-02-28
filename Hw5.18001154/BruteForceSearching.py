def str_match(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(0, n - m + 1):
        j = 0
        while j < m and pattern[j] == text[i + j]:
            j += 1
        if j == m:
            print('Found at : ', i)
    return False
text = 'abcaaabbccbcbcaabcaaab'
pattern = 'aaa'
str_match(text, pattern)