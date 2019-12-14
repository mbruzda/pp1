matrix = [[1, 2, 0],
          [0, 0, 3],
          [5, 1, 1]]



def transpose(x):
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],]
    for i in range(3):
        for j in range(3):
              matrix[j][i] = x[i][j]
        
    return matrix

x=transpose(matrix)

for i in x:
    print(i)
    
