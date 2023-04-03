rows, columns, bombs = [int(i) for i in input().split()]
matrix = [[0 for i in range(columns)] for i in range(rows)]

# matrix with the bombs
for num in range(bombs):
    b_row, b_column = [int(i) for i in input().split()]
    matrix[b_row-1][b_column-1] = '* '

# count the bombs
for index, row in enumerate(matrix):
    # rules for the first row
    if index == 0:
        for i, column in enumerate(matrix[index]):
            if i == 0:
                if column == '* ':
                    if matrix[index][i+1] != '* ':
                        matrix[index][i+1] = int(matrix[index][i+1]) + 1
                    if matrix[index+1][i] != '* ':
                        matrix[index+1][i] = int(matrix[index+1][i]) + 1
                    if matrix[index+1][i+1] != '* ':
                        matrix[index+1][i+1] = int(matrix[index+1][i+1]) + 1
            elif i == len(matrix[index]) - 1:
                if column == '* ':
                    if matrix[index][-2] != '* ':
                        matrix[index][-2] = int(matrix[index][-2]) + 1
                    if matrix[index+1][-1] != '* ':
                        matrix[index+1][-1] = int(matrix[index+1][-1]) + 1
                    if matrix[index+1][-2] != '* ':
                        matrix[index+1][-2] = int(matrix[index+1][-2]) + 1
            else:
                if column == '* ':
                    if matrix[index][i-1] != '* ':    
                        matrix[index][i-1] = int(matrix[index][i-1]) + 1
                    if matrix[index][i+1] != '* ':
                        matrix[index][i+1] = int(matrix[index][i+1]) + 1
                    if matrix[index+1][i] != '* ':    
                        matrix[index+1][i] = int(matrix[index+1][i]) + 1
                    if matrix[index+1][i+1] != '* ':    
                        matrix[index+1][i+1] = int(matrix[index+1][i+1]) + 1
                    if matrix[index+1][i-1] != '* ':    
                        matrix[index+1][i-1] = int(matrix[index+1][i-1]) + 1
    
    #rules for the last row
    elif index == len(matrix[index]):
        for i, column in enumerate(matrix[index]):
            if i == 0:
                if column == '* ':
                    if matrix[index][1] != '* ':
                        matrix[index][1] = int(matrix[index][1]) + 1
                    if matrix[index-1][i] != '* ':    
                        matrix[index-1][i] = int(matrix[index-1][i]) + 1
                    if matrix[index-1][i+1] != '* ':    
                        matrix[index-1][i+1] = int(matrix[index-1][i+1]) + 1
            elif i == len(matrix[index]) - 1:
                if column == '* ':
                    if matrix[index][-2] != '* ':
                        matrix[index][-2] = int(matrix[index][-2]) + 1
                    if matrix[index-1][-1] != '* ':
                        matrix[index-1][-1] = int(matrix[index-1][-1]) + 1
                    if matrix[index-1][-2] != '* ':
                        matrix[index-1][-2] = int(matrix[index-1][-2]) + 1
            else:
                if column == '* ':
                    if matrix[index][i-1] != '* ':
                        matrix[index][i-1] = int(matrix[index][i-1]) + 1
                    if matrix[index][i+1] != '* ':
                        matrix[index][i+1] = int(matrix[index][i+1]) + 1
                    if matrix[index-1][i] != '* ':    
                        matrix[index-1][i] = int(matrix[index-1][i]) + 1
                    if matrix[index-1][i-1] != '* ':    
                        matrix[index-1][i-1] = int(matrix[index-1][i-1]) + 1
                    if matrix[index-1][i+1] != '* ':    
                        matrix[index-1][i+1] = int(matrix[index-1][i+1]) + 1

    #rules for other rows
    else:
        for i, column in enumerate(matrix[index]):
            if i == 0:
                if column == '* ':
                    if matrix[index][i+1] != '* ':
                        matrix[index][i+1] = int(matrix[index][i+1]) + 1
                    if matrix[index-1][i] != '* ':
                        matrix[index-1][i] = int(matrix[index-1][i]) + 1
                    if matrix[index+1][i] != '* ':
                        matrix[index+1][i] = int(matrix[index+1][i]) + 1
                    if matrix[index-1][i+1] != '* ':
                        matrix[index-1][i+1] = int(matrix[index-1][i+1]) + 1
                    if matrix[index+1][i+1] != '* ':
                        matrix[index+1][i+1] = int(matrix[index+1][i+1]) + 1
                    
            elif i == len(matrix[index]) - 1:
                if column == '* ':
                    if matrix[index][-2] != '* ':
                        matrix[index][-2] = int(matrix[index][-2]) + 1
                    if matrix[index-1][-1] != '* ':
                        matrix[index-1][-1] = int(matrix[index-1][-1]) + 1
                    if matrix[index+1][-1] != '* ':
                        matrix[index+1][-1] = int(matrix[index+1][-1]) + 1
                    if matrix[index-1][-2] != '* ':
                        matrix[index-1][-2] = int(matrix[index-1][-2]) + 1
                    if matrix[index+1][-2] != '* ':
                        matrix[index+1][-2] = int(matrix[index+1][-2]) + 1
            else:
                if column == '* ':
                    if matrix[index][i-1] != '* ':
                        matrix[index][i-1] = int(matrix[index][i-1]) + 1
                    if matrix[index][i+1] != '* ':
                        matrix[index][i+1] = int(matrix[index][i+1]) + 1
                    if matrix[index+1][i] != '* ':    
                        matrix[index+1][i] = int(matrix[index+1][i]) + 1
                    if matrix[index+1][i+1] != '* ':    
                        matrix[index+1][i+1] = int(matrix[index+1][i+1]) + 1
                    if matrix[index+1][i-1] != '* ':    
                        matrix[index+1][i-1] = int(matrix[index+1][i-1]) + 1
                    if matrix[index-1][i] != '* ':
                        matrix[index-1][i] = int(matrix[index-1][i]) + 1
                    if matrix[index-1][i+1] != '* ':
                        matrix[index-1][i+1] = int(matrix[index-1][i+1]) + 1
                    if matrix[index-1][i-1] != '* ':
                        matrix[index-1][i-1] = int(matrix[index-1][i-1]) + 1

# print the final matrix

print(matrix)

for r in matrix:
    for c in r:
        if c == 0:
            print('. ', end='')
        elif c == '* ':
            print(c, end='')
        else:
            print(str(c) + ' ', end='')
    print()


# short code
n, m, k = (int(i) for i in input().split()) # строки, столбцы, кол-во мин
a = [[0 for j in range(m)] for i in range(n)] # пустая таблица из 0

for i in range(k): # перебираем кол-во мин
    rw, cl = (int(i) - 1 for i in input().split()) # записываем строку и столбец одной мины при каждом проходе
    a[rw][cl] = -1 # записываем мину по координатам столбца и колонны

for i in range(n): # перебираем строки
    for j in range(m): # перебираем столбцы 
        if a[i][j] == 0: # ячейка без мины
            for di in range(-1, 2): # перебираем соседние строки (просто цифры -1 0 1)
                for dj in range(-1, 2): # перебираем соседние столбцы (просто цифры -1 0 1)
                    ai = i + di # координата по строке
                    aj = j + dj # координата по столбцу
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1: # проверка вхождения в диапазон и мины по соседству
                        a[i][j] += 1

for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
	print()