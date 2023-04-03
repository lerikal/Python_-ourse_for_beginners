#create a matrix
matrix = []
input_str = str(input())

while input_str != 'end':
    matrix.append(input_str.split())
    input_str = str(input())

# (i-1, j), (i+1, j), (i, j-1), (i, j+1)

for i in range(len(matrix)): # index for row
    for j in range(len(matrix[i])): #index pro column 
        
        a = int(matrix[i-1][j])
        
        if i == len(matrix) - 1:
            b = int(matrix[0][j])
        else:
            b = int(matrix[i+1][j])

        c = int(matrix[i][j-1])

        if j == len(matrix) -1:
            d = int(matrix[i][0])
        else:
            d = int(matrix[i][j+1])
        
        s = a + b + c + d
        print(s, end=' ')
    
    print()
