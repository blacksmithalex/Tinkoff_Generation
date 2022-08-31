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
    elif i % 2 == 0:
        Ndays[i] = 30
    else:
        Ndays[i] = 31

comb = [[0, 1, 2], [0, 2, 1] , [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
flag = False
for c in comb:
    extra = 0
    d, m, y = r[c[0]], r[c[1]], r[c[2]]
    if m > 12:
        continue
    if (y % 4 == 0) and (y != 0):
        extra = 1
    if Ndays[m] + extra >= d:
        print(output(d, m, y))
        flag = True
if flag == False:
    print('No such date')


