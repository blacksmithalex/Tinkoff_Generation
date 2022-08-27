#S_i != 0 для любого i >= 0
#sgn[i] = -sgn[i - 1] для любого i >= 1
n = int(input())
a = [int(x) for x in input().split()]
S = [0] * n
S[0] = a[0]
count1 = 0
if S[0] <= 0:
    count1 += abs(S[0]) + 1
    S[0] = 1
for i in range(1, n):
    S[i] = S[i - 1] + a[i]
    if i % 2 == 0:
        if S[i] <= 0:
            count1 += abs(S[i]) + 1
            S[i] = 1
    else:
        if S[i] >= 0:
            count1 += S[i] + 1
            S[i] = -1

S = [0] * n
S[0] = a[0]
count2 = 0
if S[0] >= 0:
    count2 += S[0] + 1
    S[0] = -1
for i in range(1, n):
    S[i] = S[i - 1] + a[i]
    if i % 2 != 0:
        if S[i] <= 0:
            count2 += abs(S[i]) + 1
            S[i] = 1
    else:
        if S[i] >= 0:
            count2 += S[i] + 1
            S[i] = -1

print(min(count1, count2))

