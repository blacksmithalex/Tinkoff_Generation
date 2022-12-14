def output(d, m, y):
    d, m, y = str(d), str(m), str(y)
    if len(d) == 1:
        d = '0' + d
    if len(m) == 1:
        m = '0' + m
    if len(y) == 1:
        y = '0' + y
    return d + '/' + m + '/' + y

r = [int(x) for x in input().split('/')]
Ndays = [0] * 13
for i in range(0, 13):
    if i == 2:
        Ndays[i] = 28
    elif i in [1, 3, 5, 7, 8, 10, 12]:
        Ndays[i] = 31
    else:
        Ndays[i] = 30

comb = [[0, 1, 2], [0, 2, 1] , [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
res = set()
for c in comb:
    extra = 0
    d, m, y = r[c[0]], r[c[1]], r[c[2]]
    if m > 12 or m == 0 or d == 0:
        continue
    if (y % 4 == 0) and (y != 0):
        extra = 1
    if m == 2 and (Ndays[m] + extra >= d):
        res.add(output(d, m, y))
    elif Ndays[m] >= d:
        res.add(output(d, m, y))

if len(res) == 0:
    print('No such date')
else:
    for x in res:
        print(x)



