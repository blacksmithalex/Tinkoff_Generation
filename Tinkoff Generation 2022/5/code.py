#S_i != 0 для любого i >= 0
#sgn[i] = -sgn[i - 1] для любого i >= 1
n = int(input())
a = [int(x) for x in input().split()]
S = [0] * n
S[0] = a[0]
for i in range(1, n):
    S[i] = S[i - 1] + a[i]

count1, count2 = 0, 0
for i in range(n):
    if i % 2 == 0:
        if S[i] <= 0:
            count1 += abs(S[i]) + 1
    else:
        if S[i] >= 0:
            count1 += S[i] + 1

for i in range(n):
    if i % 2 != 0:
        if S[i] <= 0:
            count2 += abs(S[i]) + 1
    else:
        if S[i] >= 0:
            count2 += S[i] + 1

print(min(count1, count2))

