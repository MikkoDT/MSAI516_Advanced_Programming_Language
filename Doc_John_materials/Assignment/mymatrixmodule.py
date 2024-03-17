def matrixaddition(matrix1, matrix2):
  
  if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
    raise ValueError("Matrices must have the same dimensions for addition.")

  result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
  for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
      result[i][j] = matrix1[i][j] + matrix2[i][j]
  return result

def matrixsubtraction(matrix1, matrix2):
  
  if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
    raise ValueError("Matrices must have the same dimensions for subtraction.")

  result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
  for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
      result[i][j] = matrix1[i][j] - matrix2[i][j]
  return result

def matrixmultiplication(matrix1, matrix2):
  
  if len(matrix1[0]) != len(matrix2):
    raise ValueError("Number of columns in first matrix must match number of rows in second matrix for multiplication.")

  result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
  for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
      for k in range(len(matrix2)):
        result[i][j] += matrix1[i][k] * matrix2[k][j]
  return result
