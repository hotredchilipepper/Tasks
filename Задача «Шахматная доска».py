n,m = [int(s) for s in input().split()] # Входные данные длина,ширина доски
a = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            if j % 2 == 0:
                a[i][j] = '.'
            else:
                a[i][j] = '*'
        else:
            if j % 2 == 0:
                a[i][j] = '*'
            else:
                a[i][j] = '.'
for row in a:
    print(' '.join(row))  # На выводе получаем матрицу n*m состоящую из '.' и '*'.
