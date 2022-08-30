n = int(input())
a = [int(x) for x in input().split()]

l, Ml, prev = 1, 1, 0
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        l += 1
        if l > Ml:
            Ml = l
    else:
        if l > Ml:
            Ml = l
        l = 1

res = len(a) - l
print(res)