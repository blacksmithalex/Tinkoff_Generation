def update(a, l):
    'приводим список s символов строки ко всем одинаковм буквам l, возвращаем количество действий'
    count = 0
    while a.count(l) != len(a):
        for i in range(len(a) - 1):
            if a[i + 1] == l:
                a[i] = a[i + 1]
        count += 1
        a = a[:-1]
    return count

letters = set(a)

countm = len(a)
for l in letters:
    count = update(list(a), l)
    if count < countm:
        countm = count

print(countm)



