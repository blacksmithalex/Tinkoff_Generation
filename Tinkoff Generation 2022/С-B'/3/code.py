def isPalindrom(a):
    return a == a[::-1]

a = input()
if isPalindrom(a):
    print('YES')
else:
    i, j = 0, len(a) - 1
    diff = []
    while i < j:
        if a[i] != a[j]:
            diff.append([i, j])
        i += 1
        j -= 1
    if len(diff) != 2:
        print('NO')
    else:
        i1, j1 = diff[0]
        i2, j2 = diff[1]
        alls = set([a[i1], a[j1], a[i2], a[j2]])
        if len(alls) == 2:
            print('YES')
        else:
            print('NO')


