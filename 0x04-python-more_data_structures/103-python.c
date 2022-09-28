def square_matrix_simple(matrix=[]):
	new_matrix = matrix[:]
	new_matrix = [[val**2 for val in row] for row in matrix]
	return new_matrix
