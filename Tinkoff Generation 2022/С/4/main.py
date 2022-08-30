from math import ceil
a, b, c, d, e = [int(x) for x in input().split()]
K = int(input())
iters = K // (a + b + c + d + e)
eT, wT, qT = (d + e) * iters, (c + e) * iters, (a + ceil(b / 2)) * iters
K %= (a + b + c + d + e)
if a >= K:
    print(eT, wT, qT + K)
    quit()
qT += a
K -= a
if b >= K:
    print(eT, wT, qT + ceil(K / 2))
    quit()
qT += ceil(b / 2)
K -= b
if c >= K:
    print(eT, wT + K, qT)
    quit()
wT += c
K -= c
if d >= K:
    print(eT + K, wT, qT)
    quit()
eT += d
K -= d
if e >= K:
    print(eT + K, wT + K, qT)
    quit()
eT += e
wT += e
K -= e
print(eT, wT, qT)



