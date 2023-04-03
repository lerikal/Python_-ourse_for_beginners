n = int(input())
matrix = [[0 for j in range(n)] for i in range(n)]
a = 0

for i in range(n):
    for j in range(n):
        if j in range(a,n-a-1): # segment 1
            if j > 0: 
                matrix[i][j] = matrix[i][j-1] + 1
            else:
                matrix[i][j] = 1 
  
        elif j in range(a+1, n): # segment 2
            if j == n-1-a:
                matrix[i][j] = matrix[i][j-1] + 1
            else:
                matrix[i][j] = matrix[i-1][j] + 1
                
        elif j in range(n-a): # segment 4
            if j == i-1:
                matrix[i][j] = (n-a) * 4 * a
            elif n % 2 == 1 and i == j:
                matrix[i][j] = (n-a) * 4 * a+1
            else:
                matrix[i][j] = matrix[i-1][j] -1
        
        elif j in range(n-a, n): # segment 3
            if j < n-1:
                matrix[i][j] = matrix[i][j-1] - 1
            else:
                matrix[i][j] = matrix[i-1][j] + 1
    a += 1  
            
for row in matrix:
    for column in row:
        print(column, end=' ')
    print()
    