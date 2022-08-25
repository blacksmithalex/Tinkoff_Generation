def update(A, b, n):
    '''Функция, которая заполняет матрицу А из списка b'''
    for j in range(n):
        count = 0
        for i in range(n - 1, -1, -1):
            if count < b[j]:
                A[i][j] = 1
                count += 1
            else:
                break
    return A

def rotate(A):
    '''Поворачивает матрицу на 90 градусов без учета гравитации'''
    return A

def gravitation(A):
    '''Применяет гравитацию для A'''
    return A

def output(A):
    '''Выводит матрицу А в необходимом формате'''
    return A

n, k = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
A = [[0] * n for _ in range(n)]
A = update(A, b, n)
for x in A:
    print(*x)