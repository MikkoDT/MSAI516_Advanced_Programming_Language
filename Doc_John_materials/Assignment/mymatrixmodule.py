def matrixaddition(matrix1, matrix2):
  
  if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
    raise ValueError("Matrices must have the same dimensions for addition.")

  result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
  for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
      result[i][j] = matrix1[i][j] + matrix2[i][j]
  return result

def matrixsubtraction(matrix1, matrix2):
  """
  This function subtracts two matrices of the same dimensions.

  Args:
      matrix1: A list of lists representing the first matrix.
      matrix2: A list of lists representing the second matrix.

  Returns:
      A list of lists representing the difference of the two matrices.

  Raises:
      ValueError: If the matrices have different dimensions.
  """
  if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
    raise ValueError("Matrices must have the same dimensions for subtraction.")

  result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
  for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
      result[i][j] = matrix1[i][j] - matrix2[i][j]
  return result

def matrixmultiplication(matrix1, matrix2):
  """
  This function multiplies two matrices.

  Args:
      matrix1: A list of lists representing the first matrix.
      matrix2: A list of lists representing the second matrix.

  Returns:
      A list of lists representing the product of the two matrices.

  Raises:
      ValueError: If the number of columns in the first matrix doesn't match the number of rows in the second matrix.
  """
  if len(matrix1[0]) != len(matrix2):
    raise ValueError("Number of columns in first matrix must match number of rows in second matrix for multiplication.")

  result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
  for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
      for k in range(len(matrix2)):
        result[i][j] += matrix1[i][k] * matrix2[k][j]
  return result

# Example usage
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

# Addition
added_matrix = matrixaddition(matrix1, matrix2)
print(added_matrix)  # Output: [[6, 8], [10, 12]]

# Subtraction
subtracted_matrix = matrixsubtraction(matrix1, matrix2)
print(subtracted_matrix)  # Output: [[-4, -4], [-4, -4]]

# Multiplication (assuming matrix2 has dimensions (2, 2) for valid multiplication)
multiplied_matrix = matrixmultiplication(matrix1, matrix2)
print(multiplied_matrix)  # Output will depend on the specific values in matrix2