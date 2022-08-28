n, m, c = [int(x) for x in input().split()]
P1, P2, P3min, P3max, P4min, P4max = -1, -1, -1, -1, -1, -1
if c % 2 != 0:
    print('NO')
else:
    n, m = min(n, m), max(n, m)
    if n >= 3:
        P1 = 2 * n + 6 * m
    if m >= 3:
        P2 = 2 * m + 6 * n
    if m >= 2:
        P3min = 4 * n + 2 * m + 2 * (m // 2)
        P3max = 4 * n + 2 * m + 2 * (m - 1)
    if n >= 2:
        P4min = 4 * m + 2 * n + 2 * (n // 2)
        P4max = 4 * m + 2 * n + 2 * (n - 1)
    if c == P1 or c == P2 or P3min <= c <= P3max or P4min <= c <= P4max:
        print('YES')
    else:
        print('NO')




