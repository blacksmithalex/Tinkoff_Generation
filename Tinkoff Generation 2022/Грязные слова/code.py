def shift(a):
    return a[0] + a[-2] + a[1:-2] + a[-1]
#ord от 65 до 90, от 97 до 122
a = input()
l, r = 0, 0
flag = False
while r < len(a):
    r1 = 65 <= ord(a[r]) <= 90
    r2 = 97 <= ord(a[r]) <= 122
    if r1 or r2:
        r += 1
    else:
        if r - l > 3:
            a = a[:l] + shift(a[l: r]) + a[r:]
        while not(r1 or r2):
            r += 1
            r1 = 65 <= ord(a[r]) <= 90
            r2 = 97 <= ord(a[r]) <= 122
        l = r
if r - l > 3:
    a = a[:l] + shift(a[l: r]) + a[r:]
print(a)


