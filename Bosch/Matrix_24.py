def matrix_replace(matrix):
  
  max_value = max(max(row) for row in matrix if row)

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == -1 or matrix[i][j] == 1:
        matrix[i][j] = max_value

matrix = [
  [1, 2, 3],
  [-1, 6, 4],
  [7, -1, 1]
]

result = matrix_replace(matrix)
for row in matrix:
  print(row)
