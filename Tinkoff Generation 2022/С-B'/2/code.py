n, k = [int(x) for x in input().split()]
Msize, Mx = int(1e6), 0
x = [0] * (Msize + 1)
for _ in range(n):
    ci, xi = [int(x) for x in input().split()]
    x[xi] = ci
    if xi > Mx:
        Mx = xi
x = x[:Mx + 1]
view = [0] * len(x)
view[0] = sum(x[:k + 1])

for i in range(1, len(x)):
    if i - k - 1 < 0:
        if i + k >= len(x):
            view[i] = view[i - 1]
        else:
            view[i] = view[i - 1] + x[i + k]
    else:
        if i + k >= len(x):
            view[i] = view[i - 1] - x[i - k - 1]
        else:
            view[i] = view[i - 1] - x[i - k - 1] + x[i + k]

print(max(view))



