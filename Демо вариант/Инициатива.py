a = 'Tfifnok'
res = ''
for i in range(0, len(a), 2):
    res += a[i]
if i == len(a) - 1:
    for j in range(len(a) - 2, 0, -2):
        res += a[j]
else:
    for j in range(len(a) - 1, 0, -2):
        res += a[j]

print(res)


